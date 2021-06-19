
from flask import Blueprint, render_template, jsonify, redirect, url_for, flash
from faker import Faker
from exam import db
from exam.forms.exam import generate_exam, search_add
from exam.models.exam import Paper
from exam.models.problem import Problem

manage_exam_bp = Blueprint('manage_exam', __name__)


@manage_exam_bp.route('/gen_exam_home', methods=['GET', 'POST'])
def home(chosen_prob=[]):
    form = generate_exam()
    fake = Faker()
    if form.submit.data:
        paper = Paper(name=form.name.data, paper_id=fake.pyint(), subject=form.subject.data ,strt_t=form.strt_time.data, end_t=form.end_time.data,
                      )
        if len(chosen_prob):
            paper.problems.append(chosen_prob)
        db.session.add(paper)
        db.session.commit()
        flash('生成成功')

    return render_template('exam_view/gen_exam.html', form=form)


@manage_exam_bp.route('/problem/add')
def exam_search_add():
    form = search_add()
    problems = Problem.query.all()
    if form.submit.data:
        chosen_pro = Problem.query.filter(Problem.chosen == 1).all()

        return redirect(url_for('home'), )
    return render_template('exam_view/exam_search_add.html', form=form, problems=problems)


# 选择题目加入试卷
@manage_exam_bp.route('/problem/<int:problem_id>/choose', methods=['PATCH'])
# @login_required
def choose_prob(problem_id):
    problem = Problem.query.get_or_404(problem_id)
    # if current_user != item.author:
    #     return jsonify(message=_('Permission denied.')), 403

    problem.chosen = not problem.chosen  # 试卷加入题目
    db.session.commit()
    return jsonify(message=_('Problem Chosen.'))

# @manage_exam_bp.route('/add_pro_exam')
# def home():
#     form = generate_exam()
#     return render_template('exam_view/gen_exam.html', form=form)
