from flask import Blueprint
from exam import db
from exam.forms.problem import ProblemForm
from exam.models.problem import Problem, Tag
from flask import render_template, request, flash, redirect, url_for


problem_bp = Blueprint('problem', __name__)


@problem_bp.route('/')
def home():
    problems = Problem.query.all()
    return render_template('problem/index.html', problems=problems)


@problem_bp.route('/render-problem-edit', methods=['POST'])
def render_edit_form():
    problem_id = int(request.form.get('id'))
    form = ProblemForm()
    form.problem_id.data = problem_id

    if problem_id != 0:
        problem = Problem.query.filter_by(problem_id=str(problem_id)).first()

        form.type.data = str(problem.type)
        form.text.data = problem.text
        form.choice_A.data = problem.choice_A
        form.choice_B.data = problem.choice_B
        form.choice_C.data = problem.choice_C
        form.choice_D.data = problem.choice_D
        form.solution.data = problem.solution
        form.adder.data = problem.adder
        form.tags.data = ' '.join([x.tag_name for x in problem.tags])

    return render_template('problem/problem_edit_form.html', form=form)


@problem_bp.route('/delete-problem/<int:problem_id>', methods=['POST'])
def delete_problem(problem_id):
    problem = Problem.query.filter_by(problem_id=problem_id).first()
    if problem is not None:
        for tag in problem.tags:
            problem.tags.remove(tag)
            if not tag.problems:
                db.session.delete(tag)
        db.session.delete(problem)
        db.session.commit()
    flash('删除题目成功。')
    return redirect(url_for('.home'))


@problem_bp.route('/edit-problem', methods=['POST'])
def edit_problem():
    form = ProblemForm()
    problem_id = form.problem_id.data

    if form.validate_on_submit():
        problem = Problem()
        if problem_id != 0:
            problem = Problem.query.filter_by(problem_id=problem_id).first()

        problem.type = form.type.data
        problem.text = form.text.data
        problem.choice_A = form.choice_A.data
        problem.choice_B = form.choice_B.data
        problem.choice_C = form.choice_C.data
        problem.choice_D = form.choice_D.data
        problem.solution = form.solution.data
        problem.adder = form.adder.data

        if problem_id == 0:
            db.session.add(problem)

        new_tag_names = set(form.tags.data.split())
        for tag in problem.tags:
            if tag.tag_name not in new_tag_names:
                problem.tags.remove(tag)
                if not tag.problems:
                    db.session.delete(tag)
        for tag_name in new_tag_names:
            tag = Tag.query.filter_by(tag_name=tag_name).first()
            if tag is None:
                tag = Tag(tag_name=tag_name)
            if tag not in problem.tags:
                problem.tags.append(tag)

        db.session.commit()
        flash('题目更新成功。')
        return 'OK'

    return render_template('problem/problem_edit_form.html', form=form)