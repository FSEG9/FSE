from flask import Blueprint
from exam import db
from exam.models.exam import Paper, exam_has_problem
from flask import render_template, request, flash, redirect, url_for

view_exam_bp = Blueprint('view_exam', __name__)


@view_exam_bp.route('/')
def home():
    exams = Paper.query.all()
    return render_template('exam/view_exam.html', exams=exams)