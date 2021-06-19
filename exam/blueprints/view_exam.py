from flask import Blueprint
from exam import db
from exam.models.exam import Paper, exam_has_problem
from flask import render_template, request, flash, redirect, url_for
from datetime import datetime
import time

view_exam_bp = Blueprint('view_exam', __name__)


@view_exam_bp.route('/')
def home():
    exams = Paper.query.all()
    return render_template('exam/view_exam.html', exams=exams)


@view_exam_bp.route('/information/<int:paper_id>')
def show_information(paper_id):
    exam = Paper.query.filter_by(paper_id=paper_id).first()
    dt1 = time.time()
    n_time = datetime.strftime(exam.strt_t, "%Y-%m-%d")
    dt2 = time.mktime(time.strptime(n_time, "%Y-%m-%d"))  # 开始时间
    n_time = datetime.strftime(exam.end_t, "%Y-%m-%d")
    dt3 = time.mktime(time.strptime(n_time, "%Y-%m-%d"))  # 结束时间

    if dt1<dt2:
        label = 0
    elif dt1>dt3:
        label = 1
    else:
        label = 2
    return render_template('exam/exam_info.html', exam=exam, label=label)