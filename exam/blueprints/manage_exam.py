from flask import Blueprint, render_template, jsonify, redirect, url_for, flash
from faker import Faker
from exam import db
from exam.forms.exam import generate_exam, search_add
from exam.models.exam import Paper
from exam.models.problem import Problem, Tag

manage_exam_bp = Blueprint('manage_exam', __name__)


@manage_exam_bp.route('/gen_exam_home', methods=['GET', 'POST'])
def home():
    chosen_pro = Problem.query.filter(Problem.chosen == 1).all()
    # print(chosen_pro)
    tags = Tag.query.all()
    form = generate_exam()
    fake = Faker()
    if form.condition.data:
        # print(form.chosenTag.data)
        # print("1")
        # print(form.num_problem.data)
        # print("2")
        chosen_tag = Tag.query.filter(Tag.tag_id == form.chosenTag.data).first()
        num = form.num_problem.data
        i=0
        for problem in chosen_tag.problems:
            if i == num:
                break
            i = i + 1
            problem.chosen = 1
        db.session.commit()
    if form.submit.data:
        # try:
            start_time = form.start_date.data + "-" + form.start_time.data
            end_time = form.end_date.data + "-" + form.end_time.data

            paper = Paper(name=form.name.data, paper_id=fake.pyint(), subject=form.subject.data, strt_t=start_time,
                          end_t=end_time
                          )
            # print("bbb")
            if len(chosen_pro):
                for item in chosen_pro:
                    paper.problems.append(item)
                # print("aaa")
            db.session.add(paper)
            db.session.commit()
            for problem in chosen_pro:
                problem.chosen = False
            db.session.commit()
            flash('生成成功')
        # except Exception as e:
        #     flash('错误操作')  # to be continued: error page...
    return render_template('exam_view/gen_exam.html', form=form, tags=tags, chosen_pro=chosen_pro)


@manage_exam_bp.route('/problem/add', methods=['GET', 'POST'])
def exam_search_add():
    form = search_add()
    problems = Problem.query.all()
    if form.submit.data:
        return redirect(url_for('.home'))
    return render_template('exam_view/exam_search_add.html', form=form, problems=problems)


@manage_exam_bp.route('/problem/<int:problem_id>/choose', methods=['PATCH'])
# @login_required
def choose_prob(problem_id):
    problem = Problem.query.get_or_404(problem_id)
    problem.chosen = not problem.chosen  # 试卷加入题目
    db.session.commit()
    return jsonify(message=_('Problem Chosen.'))


@manage_exam_bp.route('/select_condition', methods=['GET'])
# @login_required
def select_condition():
    return render_template('exam_view/auto_condition_select.html')
