from datetime import date
from flask import Blueprint, render_template
from flask_login import login_required, current_user
from models import Subject, Deadline

dashboard = Blueprint("dashboard", __name__)

@dashboard.route("/")
@login_required
def index():
    subjects = Subject.query.filter_by(user_id=current_user.id).order_by(Subject.name).all()
    today = date.today()

    upcoming = (
        Deadline.query
        .filter(Deadline.user_id == current_user.id, Deadline.exam_date >= today)
        .order_by(Deadline.exam_date)
        .all()
    )
    for d in upcoming:
        d.days_left = (d.exam_date - today).days

    past_count = Deadline.query.filter(
        Deadline.user_id == current_user.id, Deadline.exam_date < today
    ).count()

    next_deadline = upcoming[0] if upcoming else None
    days_left = next_deadline.days_left if next_deadline else None

    return render_template(
        "dashboard/index.html",
        subjects=subjects,
        upcoming=upcoming[:6],
        next_deadline=next_deadline,
        days_left=days_left,
        upcoming_count=len(upcoming),
        past_count=past_count,
    )

