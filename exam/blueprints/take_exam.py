from flask import Blueprint
from flask import render_template, request, flash, redirect, url_for
from exam.models.problem import Problem

take_exam_bp = Blueprint('take_exam', __name__)


@take_exam_bp.route('/')

def home():
#<<<<<<< HEAD
    problems = Problem.query.filter_by().all() #fty：这里我不会选题目
    return render_template('exam/take_exam.html',problems=problems)

@take_exam_bp.route('/answerlist')

def exam_answerlist():

    return render_template('exam/answerlist.html')
#=======
    return '这是学生参加考试的主页面。'


@take_exam_bp.route('/take_exam')
def take_exam():
    return '这是开始考试的界面'


@take_exam_bp.route('/show_exam')
def show_exam():
    problems = Problem.query.filter_by().all()  # fty：这里我不会选题目
    return render_template('exam/take_exam.html', problems=problems)
#>>>>>>> 14f5db0cfb24df424ce7f252a0f0ef822ad0b127
