"""教师管理考试的相关视图函数"""
import ast
import re

from flask import Blueprint, render_template, jsonify, redirect, url_for, flash, request
from faker import Faker
from exam import db
from exam.forms.exam import generate_exam, search_add
from exam.models.exam import Paper
from exam.models.problem import Problem, Tag

manage_exam_bp = Blueprint('manage_exam', __name__)


@manage_exam_bp.route('/gen_exam_home', methods=['GET', 'POST'])
def home():
    chosen_proid = [0, 0]  # 保证传入的是列表
    print(chosen_proid)
    return redirect(url_for('manage_exam.paper_has_pro', chosen_proid=chosen_proid))


@manage_exam_bp.route('/problem_add/<chosen_proid>', methods=['GET', 'POST'])
def exam_search_add(chosen_proid):
    chosen_proid = ast.literal_eval(chosen_proid)
    problems = Problem.query.filter(~Problem.problem_id.in_(chosen_proid)).all()
    if request.method == 'POST':
        for problem in problems:
            proid = request.form.getlist(str(problem.problem_id))
            # print(proid)
            if len(proid):
                print(proid)
                chosen_proid.append(proid[0])
        return redirect(url_for('manage_exam.paper_has_pro', chosen_proid=chosen_proid))
    print(chosen_proid)
    return render_template('exam_view/exam_search_add.html', chosen_proid=chosen_proid, problems=problems)


@manage_exam_bp.route('/added_paper/<chosen_proid>', methods=['GET', 'POST'])
def paper_has_pro(chosen_proid):
    print(chosen_proid)
    tags = Tag.query.all()
    # chosen_proid = re.findall(r'\d', chosen_proid)
    print(len(chosen_proid))
    chosen_proid = ast.literal_eval(chosen_proid)
    problems = []
    if len(chosen_proid) != 2:
        problems = Problem.query.filter(Problem.problem_id.in_(chosen_proid))
    if request.method == 'POST':
        if request.form.get('cancel'):
            print("取消")
            return redirect(url_for('manage_exam.paper_has_pro', chosen_proid=chosen_proid))
        if request.form.get('clear'):
            chosen_proid = [0,0]
            return redirect(url_for('manage_exam.paper_has_pro', chosen_proid=chosen_proid))
        if request.form.get('gen_exam'):
            print("提交生成测试")
            if request.method == 'POST':
                name = request.form.get('name')
                subject = request.form.get('subject')
                start_date = request.form.get('start_date')
                start_time = request.form.get('start_time')
                end_date = request.form.get('end_date')
                end_time = request.form.get('end_time')
                print(name)
                print(subject)
                print(start_time)
                if len(chosen_proid) != 2 and len(name) and len(subject) and len(start_date) and len(end_date) :
                    print("222222")
                    start_time = start_date + "-" + start_time
                    end_time = end_date + "-" + end_time
                    fake = Faker()
                    id = fake.pyint()
                    while Paper.query.filter(Paper.paper_id == id).first() is not None:
                        id = fake.pyint()
                    paper = Paper(name=name, paper_id=id, subject=subject, strt_t=start_time,
                                  end_t=end_time
                                  )
                    for problem in problems:
                        paper.problems.append(problem)
                    db.session.add(paper)
                    db.session.commit()

                    flash('生成成功')
                    chosen_proid = [0,0]
                    return redirect(url_for('manage_exam.paper_has_pro', chosen_proid=chosen_proid))
                elif len(chosen_proid) == 2:
                    flash('请添加题目')
                else:
                    flash('请填入完整信息')
                    return redirect(url_for('manage_exam.paper_has_pro', chosen_proid=chosen_proid))
        if request.form.get('auto_select_submit'):
            print("提交自动选择条件")
            chosen_tag = Tag.query.filter(Tag.tag_id == request.form.get('chosenTag')).first()
            chosen_type = request.form.get('type_problem')
            chosen_type = int(chosen_type)
            num = request.form.get('num_problem')
            num = int(num)
            i = 0
            for problem in chosen_tag.problems:
                if problem.problem_id in chosen_proid:
                    continue
                if i == num:
                    break
                if chosen_type == -1:
                    i = i + 1
                    chosen_proid.append(problem.problem_id)
                    continue
                if problem.type == chosen_type:
                    i = i + 1
                    chosen_proid.append(problem.problem_id)
            if i<num-1:
                flash('题目数量不足 仅加入'+str(i)+'道题')
            return redirect(url_for('manage_exam.paper_has_pro', chosen_proid=chosen_proid))
        else:
            print("删除题目")
            for problem in problems:
                name = problem.problem_id
                if request.form.get(str(name)):
                    print(str(problem.problem_id))
                    if problem.problem_id in chosen_proid:
                        chosen_proid.remove(problem.problem_id)
                    else:
                        chosen_proid.remove(str(problem.problem_id))
                    break
            return redirect(url_for('manage_exam.paper_has_pro', chosen_proid=chosen_proid))
    return render_template('exam_view/gen_exam.html', tags=tags, chosen_proid=chosen_proid, problems=problems)
