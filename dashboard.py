from flask import Blueprint, render_template
from flask_login import login_required, current_user
from models import Subject, Deadline
from datetime import date

dashboard = Blueprint("dashboard", __name__)

@dashboard.route("/")
@login_required
def index():
    subjects = Subject.query.filter_by(user_id=current_user.id).all()
    deadlines = Deadline.query.filter_by(user_id=current_user.id).order_by(Deadline.exam_date).all()

    today = date.today()
    days_left = None
    if deadlines:
        next_exam = deadlines[0].exam_date
        days_left = (next_exam - today).days

    return render_template("dashboard/index.html", subjects=subjects, deadlines=deadlines, days_left=days_left)