from flask import Flask
from config import Config
from models import db
from flask_login import LoginManager

login_manager = LoginManager()
login_manager.login_view = "auth.login"
login_manager.login_message = "Log in to study"

@login_manager.user_loader
def load_user(user_id):
    from models import User
    return User.query.get(int(user_id))

def create_app(config_class=Config):
    app=Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    login_manager.init_app(app)

    from auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix="/auth")

    from dashboard import dashboard as dashboard_blueprint
    app.register_blueprint(dashboard_blueprint)

    from subjects import subjects as subjects_blueprint
    app.register_blueprint(subjects_blueprint)

    return app