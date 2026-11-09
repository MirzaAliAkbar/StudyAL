from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_required, current_user
from models import db, Subject, Deadline
from datetime import datetime

subjects = Blueprint("subjects", __name__)

@subjects.route("/subjects", methods=["GET", "POST"])
@login_required
def manage():
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        if name:
            existing = Subject.query.filter_by(user_id=current_user.id, name=name).first()
            if existing:
                flash("Subject already exists")
            else:
                subject = Subject(name=name, user_id=current_user.id)
                db.session.add(subject)
                db.session.commit()
                flash(f"Added {name}")
        return redirect(url_for("subjects.manage"))
    user_subjects = Subject.query.filter_by(user_id=current_user.id).all()
    return render_template("subjects/index.html", subjects = user_subjects)

@subjects.route("/subjects/<int:subject_id>/delete")
@login_required
def delete(subject_id):
    subject = Subject.query.filter_by(id=subject_id, user_id=current_user.id).first_or_404()
    db.session.delete(subject)
    db.session.commit()
    return redirect(url_for("subjects.manage"))

@subjects.route("/deadlines", methods=["GET", "POST"])
@login_required
def deadlines():
    if request.method == "POST":
        title = request.form.get("title", "").strip()
        subject_id = request.form.get("subject_id", "")
        exam_date = request.form.get("exam_date", "")
        dtype = request.form.get("type", "exam")

        if title and subject_id and exam_date:
            deadline = Deadline(
                title=title,
                subject_id=int(subject_id),
                exam_date=datetime.strptime(exam_date, "%Y-%m-%d").date(),
                type=dtype,
                user_id=current_user.id

            )
            db.session.add(deadline)
            db.session.commit()
            flash("Deadline added")
        return redirect(url_for("subjects.deadlines"))

    user_subjects = Subject.query.filter_by(user_id=current_user.id).all()
    user_deadlines = Deadline.query.filter_by(user_id=current_user.id).order_by(Deadline.exam_date).all()
    return render_template("subjects/deadlines.html", subjects=user_subjects, deadlines=user_deadlines)