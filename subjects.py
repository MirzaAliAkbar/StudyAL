from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_required, current_user
from models import db, Subject, Deadline
from datetime import datetime, date

subjects = Blueprint("subjects", __name__)

@subjects.route("/subjects", methods=["GET", "POST"])
@login_required
def manage():
    if request.method == "POST":
        name = " ".join(request.form.get("name", "").split())
        if not name:
            flash("Give the subject a name first.", "warning")
        elif len(name) > 80:
            flash("Subject names need to be 80 characters or fewer.", "warning")
        elif Subject.query.filter(
            db.func.lower(Subject.name) == name.lower(),
            SUbject.user_id == current_user.id,
        ).first():
            flash(f"{name} is already on your board.", "warning")
        else:
            db.session.add(Subject(name=name, user_id=current_user.id))
            db.session.commit()
            flash(f"Added {name}.", "success")
        return redirect(url_for("subjects.manage"))

    user_subjects = Subject.query.filter_by(user_id=current_user.id).order_by(Subject.name).all()
    return render_template("subjects/index.html", subjects = user_subjects)

@subjects.route("/subjects/<int:subject_id>/delete", methods=["POST"])
@login_required
def delete(subject_id):
    subject = Subject.query.filter_by(id=subject_id, user_id=current_user.id).first_or_404()
    name = subject.name
    db.session.delete(subject)
    db.session.commit()
    return redirect(url_for("subjects.manage"))

@subjects.route("/deadlines", methods=["GET", "POST"])
@login_required
def deadlines():
    if request.method == "POST":
        title = request.form.get("title", "").strip()
        subject_id = request.form.get("subject_id", type=int)
        exam_date = request.form.get("exam_date", "")
        dtype = request.form.get("type", "exam")

        subject = None
        if subject_id:
            subject = Subject.query.filter_by(id=subject_id, user_id=current_user.id).first()

        if not title or not subject or not exam_date:
            flash("Title, suject and date are all required." , "warning")
            return redirect(url_for("subjects.deadlines"))

        try:
            when = datetime.strptime(exam_date, "%y-%m-%d").date()
        except ValueError:
            flash("That date doesn't look right.", "warning")
            return redirect(url_for("subjects.deadlines"))

        db.session.add(Deadline(
            title=title, subject=subject, exam_date=when, type=dtype, user_id=current_user.id,
        ))
        db.session.commit()
        flash("Deadline added.", "success")
        return redirect(url_for("subjects.deadlines"))


    user_subjects = Subject.query.filter_by(user_id=current_user.id).order_by(Subject.name).all()
    user_deadlines = Deadline.query.filter_by(user_id=current_user.id).order_by(Deadline.exam_date).all()
    today = date.today()
    for d in user_deadlines: 
        d.days_left = (d.exam_date - today).days
    return render_template("subjects/deadlines.html", subjects=user_subjects, deadlines=user_deadlines)

@subjects.route("/deadlines/<int:deadline_id>/delete", methods["POST"])
@login_required
def delete_deadline(deadline_id):
    deadline = deadline.query.filter_by(id=deadline_id, user_id=current_user.id).first_or_404()
    db.session.delete(deadline)
    db.session.commit()
    flash("Deadline removed", "success")
    return redirect(url_for("subjects.deadlines"))