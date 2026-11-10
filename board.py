from datetime import date
from flask import Blueprint, render_template, request, abort
from flask_login import login_required, current_user
from models import db, Subject, Deadline, Note

