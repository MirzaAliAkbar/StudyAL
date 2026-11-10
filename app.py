from flask import Flask, render_template
from config import Config
from models import db
from flask_login import LoginManager

login_manager = LoginManager()
login_manager.login_view = "auth.login"
login_manager.login_message = "Log in to study"
login_manager.login_message_category = "warning"

@login_manager.user_loader
def load_user(user_id):
    from models import User
    return db.session.get(User, int(user_id))

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    login_manager.init_app(app)

    from auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix="/auth")

    from dashboard import dashboard as dashboard_blueprint
    app.register_blueprint(dashboard_blueprint)

    from subjects import subjects as subjects_blueprint
    app.register_blueprint(subjects_blueprint)

    from board import board as board_blueprint
    app.register_blueprint(board_blueprint)

    with app.app_context():
        db.create_all()

    @app.errorhandler(404)
    def not_found(error):
        return render_template("errors/404.html"), 404

    @app.errorhandler(500)
    def server_error(error):
        db.session.rollback()
        return render_template("errors/500.html"), 500

    return app

if __name__ == "__main__":
    create_app().run(debug=True)