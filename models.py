from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash,check_password_hash
from datetime import datetime

db = SQLAlchemy()

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)

    subjects = db.relationship("Subject", backref="user", cascade="all, delete-orphan")
    deadlines = db.relationship("Deadline", backref="user", cascade="all, delete-orphan")
    notes = db.relationship("Note", backref="user", cascade="all, delete-orphan")

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Subject(db.Model):
    __table_args__ = (db.UniqueConstraint("user_id", "name", name="uq_subject_user_name"),)

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    name = db.Column(db.String(80), nullable=False)
    x = db.Column(db.Float)
    y = db.Column(db.Float)

    deadlines = db.relationship(
        "Deadline", backref="subject", cascade="all, delete-orphan", order_by="Deadline.exam_date",
    )
    notes = db.relationship(
        "Note", backref="subject", cascade="all, delete-orphan", order_by="Deadline.exam_date",
    )



class Deadline(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    subject_id = db.Column(db.Integer,  db.ForeignKey("subject.id"), nullable=False)
    title = db.Column(db.String(120), nullable=False)
    exam_date = db.Column(db.Date, nullable=False)
    type = db.Column(db.String(40), default="exam")
    x = db.Column(db.Float)
    y = db.Column(db.Float)


class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(200), nullable=False)
    filepath = db.Column(db.String(500), nullable=False)
    text = db.Column(db.Text, default="")
    subject_id = db.Column(db.Integer, db.ForeignKey("subject.id"), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    x = db.Column(db.Float)
    y = db.Column(db.Float)
