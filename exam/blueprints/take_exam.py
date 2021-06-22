from flask import Blueprint
from flask import render_template

from exam.models.exam import exam_has_problem, Paper
from exam.models.problem import Problem

take_exam_bp = Blueprint('take_exam', __name__)


@take_exam_bp.route('/', methods=['GET', 'POST'])
def home():
    return '没用的界面'


@take_exam_bp.route('/<int:exam_id>', methods=['GET', 'POST'])
def take_exam(exam_id):
    problems = Paper.query.filter_by(paper_id=exam_id).first().problems
    return render_template('exam/take_exam.html', problems=problems)


# @take_exam_bp.route('/gen_answer_paper', methods=['GET', 'POST'])
# def gen_answer():



@take_exam_bp.route('/show_exam/<int:exam_id>')
def show_exam(exam_id):
    problems = Paper.query.filter_by(paper_id=exam_id).first().problems
    return render_template('exam/show_list.html', problems=problems)

