from flask import Blueprint
from exam.forms.take_exam import ProblemForm
from flask import render_template, request, flash, redirect, url_for

take_exam_bp = Blueprint('take_exam', __name__)


@take_exam_bp.route('/')

def home():
    form = ProblemForm()

    return render_template('exam/take_exam.html',form=form)

@take_exam_bp.route('/answerlist')

def exam_answerlist():
    form = ProblemForm()

    return render_template('exam/answerlist.html',form = form)