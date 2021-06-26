from flask import Blueprint
from flask import render_template, request, url_for, redirect, flash

from exam import db
from exam.forms.answer import PaperForm, AnswerForm
from exam.models.exam import exam_has_problem, Paper
from exam.models.problem import Problem
from exam.models.answer import Anspa_prob_answer, Anspaper
import time

take_exam_bp = Blueprint('take_exam', __name__)


@take_exam_bp.route('/', methods=['GET', 'POST'])
def home():
    return '没用的界面'


@take_exam_bp.route('/<int:exam_id>', methods=['GET', 'POST'])
def take_exam(exam_id):
    problems = Paper.query.filter_by(paper_id=exam_id).first().problems
    paper = Paper.query.filter_by(paper_id=exam_id).first()
    length = len(problems)
    dt3 = time.mktime(paper.end_t.timetuple())
    dt1 = time.time()
    t = int(dt3-dt1)
    # print(t)
    if request.method == 'POST':
        answerpaper = Anspaper(paper_id=exam_id, student_id=1)
        db.session.add(answerpaper)
        db.session.commit()
        fullscore = 0
        for problem in problems:
            answer = ""
            score = 0
            if problem.type != 2:
                answer = request.form.get(str(problem.problem_id))
                if answer == problem.solution:
                    score = 1
                    fullscore += 1
                # print(answer)
            else:
                answers = request.form.getlist(str(problem.problem_id))
                for ans in answers:
                    answer += ans
                if answer == problem.solution:
                    score = 1
                    fullscore += 1
            a = Anspa_prob_answer(problem_id=problem.problem_id, answer=answer, anspaper_id=answerpaper.anspaper_id, score=score)
            db.session.add(a)
            answerpaper.Answers.append(a)
            answerpaper.score_all = fullscore
        db.session.add(answerpaper)
        db.session.commit()
        paper.end = True
        db.session.commit()
        flash('提交成功.')
        return redirect(url_for('view_exam.home'))
    return render_template('exam/take_exam.html', exam=paper, problems=problems, exam_id=exam_id, length=length, t=t)


@take_exam_bp.route('/show_exam/<int:exam_id>')
def show_exam(exam_id):
    paper = Paper.query.filter_by(paper_id=exam_id).first()
    problems = Paper.query.filter_by(paper_id=exam_id).first().problems
    answerpaper = Anspaper.query.filter_by(paper_id=paper.paper_id).first() #有学生id之后再改
    # print(type(answerpaper.Answers))
    # for problem in problems:
    #     answer = answerpaper.Answers.filter_by(problem_id=problem.problem_id).first().answer
    #     right = problem.solution
        # if answer==right:

    return render_template('exam/show_list.html', problems=problems, exam=paper, answerpaper=answerpaper)

