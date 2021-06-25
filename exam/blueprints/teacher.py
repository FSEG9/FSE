from flask import Blueprint
from flask import render_template, request, flash, redirect, url_for
from datetime import datetime
import time

from sqlalchemy import desc

from exam import db
from exam.models.exam import Paper
from exam.models.answer import ProbAnalysis, Anspaper

teacher_bp = Blueprint('teacher', __name__)


@teacher_bp.route('/', methods=['GET', 'POST'])
def home():
    dt1 = time
    exams = Paper.query.order_by(desc(Paper.end_t)).all()
    return render_template('teacher/view_exam.html', exams=exams, time=dt1)

@teacher_bp.route('/information/<int:paper_id>')
def show_information(paper_id):
    exam = Paper.query.filter_by(paper_id=paper_id).first()
    dt1 = time.time()
    dt2 = time.mktime(exam.strt_t.timetuple())  # 开始时间
    dt3 = time.mktime(exam.end_t.timetuple())  # 结束时间
    length = len(exam.problems)
    anspapers = exam.anspapers.order_by(Anspaper.score_all)
    if dt1<dt2:
        label = 0
    elif dt1>dt3:
        label = 2
    else:
        label = 1
    t = int(int(dt3 - dt2) / 60)
    return render_template('teacher/exam_info.html', exam=exam, label=label, length=length, t=t, anspapers=anspapers)

@teacher_bp.route('/show_exam/<int:paper_id>', methods=['GET', 'POST'])
def show_exam(paper_id):
    exam = Paper.query.filter_by(paper_id=paper_id).first()
    problems = exam.problems
    if exam.anlsflag == False:#每道题的解答结果还未分析
        answerpapers = Anspaper.query.filter_by(paper_id=paper_id).all()
        totalnum = Anspaper.query.filter_by(paper_id=paper_id).count()
        totalscore = 0
        for answerpaper in answerpapers:#计算平均分
            totalscore += answerpaper.score_all
        if totalnum == 0:
            exam.score = 0
        else:
            exam.score = totalscore / totalnum
        for problem in problems:#计算每道题的解答结果
            totalscore = 0
            null_count = 0
            t_count = 0
            f_count = 0
            a_count = 0
            b_count = 0
            c_count = 0
            d_count = 0
            if problem.type == 0:
                for answerpaper in answerpapers:
                    answer = answerpaper.Answers.filter_by(problem_id=problem.problem_id).first().answer
                    totalscore += answerpaper.Answers.filter_by(problem_id = problem.problem_id).first().score
                    if answer == "T":
                        t_count += 1
                    elif answer == "F":
                        f_count += 1
                    else:
                        null_count += 1
            elif problem.type == 1:
                for answerpaper in answerpapers:
                    answer = answerpaper.Answers.filter_by(problem_id = problem.problem_id).first().answer
                    totalscore += answerpaper.Answers.filter_by(problem_id=problem.problem_id).first().score
                    if answer == "A":
                        a_count += 1
                    elif answer == "B":
                        b_count += 1
                    elif answer == "C":
                        c_count += 1
                    elif answer == "D":
                        d_count += 1
                    else:
                        null_count += 1
            else:
                for answerpaper in answerpapers:
                    answer = answerpaper.Answers.filter_by(problem_id = problem.problem_id).first().answer
                    totalscore += answerpaper.Answers.filter_by(problem_id=problem.problem_id).first().score
                    if answer == "A":
                        a_count += 1
                    elif answer == "B":
                        b_count += 1
                    elif answer == "C":
                        c_count += 1
                    elif answer == "D":
                        d_count += 1
                    if len(answer) == 0:
                        null_count += 1
            if totalnum == 0:
                accuracy = 0
            else:
                accuracy = totalscore / totalnum
            analysis = ProbAnalysis(exam_id=exam.paper_id, problem_id=problem.problem_id, A_count=a_count,
                                    B_count=b_count, C_count=c_count, D_count=d_count, T_count=t_count, F_count=f_count,
                                    NULL_count=null_count, accuracy=accuracy)
            db.session.add(analysis)
            db.session.commit()
        exam.anlsflag = True
        db.session.commit()
    exam = Paper.query.filter_by(paper_id=paper_id).first()
    return render_template('teacher/show_exam.html', exam=exam)








