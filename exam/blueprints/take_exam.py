from flask import Blueprint
from flask import render_template, request, url_for, redirect, flash

from exam import db
from exam.forms.answer import PaperForm, AnswerForm
from exam.models.exam import exam_has_problem, Paper
from exam.models.problem import Problem
from exam.models.answer import Anspa_prob_answer, Anspaper

take_exam_bp = Blueprint('take_exam', __name__)


@take_exam_bp.route('/', methods=['GET', 'POST'])
def home():
    return '没用的界面'


@take_exam_bp.route('/<int:exam_id>', methods=['GET', 'POST'])
def take_exam(exam_id):
    problems = Paper.query.filter_by(paper_id=exam_id).first().problems
    if request.method == 'POST':
        answerpaper = Anspaper(paper_id=exam_id)
        db.session.add(answerpaper)
        db.session.commit()
        for problem in problems:
            answer = request.form.get(str(problem.problem_id))
            # print(answer)
            a = Anspa_prob_answer(problem_id=problem.problem_id, answer=answer, anspaper_id=answerpaper.anspaper_id)
            db.session.add(a)
            answerpaper.Answers.append(a)
        db.session.add(answerpaper)
        db.session.commit()
        flash('提交成功.')
        return redirect(url_for('view_exam.finish_exam', paper_id=exam_id))
    return render_template('exam/take_exam.html', problems=problems, exam_id=exam_id)


@take_exam_bp.route('/show_exam/<int:exam_id>')
def show_exam(exam_id):
    problems = Paper.query.filter_by(paper_id=exam_id).first().problems
    return render_template('exam/show_exam.html', problems=problems)


# @take_exam_bp.route('/show_exa')
# def exam_answers(exam_id):
#     problems = Paper.query.filter_by(paper_id=exam_id).first().problems
#     return render_template('exam/show_exam.html', problems=problems)
