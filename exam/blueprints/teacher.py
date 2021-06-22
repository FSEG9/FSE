from flask import Blueprint
from flask import render_template, request, flash, redirect, url_for
from datetime import datetime
import time
from exam import db
from exam.models.exam import Paper
from exam.models.answer import ProbAnalysis, Anspaper

teacher_bp = Blueprint('teacher', __name__)


@teacher_bp.route('/', methods=['GET', 'POST'])
def home():
    exams = Paper.query.all()
    return render_template('teacher/view_exam.html', exams=exams)

@teacher_bp.route('/information/<int:paper_id>')
def show_information(paper_id):
    exam = Paper.query.filter_by(paper_id=paper_id).first()
    dt1 = time.time()
    n_time = datetime.strftime(exam.strt_t, "%Y-%m-%d")
    dt2 = time.mktime(time.strptime(n_time, "%Y-%m-%d"))  # 开始时间
    n_time = datetime.strftime(exam.end_t, "%Y-%m-%d")
    dt3 = time.mktime(time.strptime(n_time, "%Y-%m-%d"))  # 结束时间

    if dt1<dt2:
        label = 0
    elif dt1>dt3:
        label = 2
    else:
        label = 1
    return render_template('teacher/exam_info.html', exam=exam, label=label)

@teacher_bp.route('/show_exam/<int:paper_id>', methods=['GET', 'POST'])
def show_exam(paper_id):
    exam = Paper.query.filter_by(paper_id=paper_id).first()
    problems = Paper.query.filter_by(paper_id=paper_id).first().problems
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
            analysis = ProbAnalysis()
            analysis.exam_id = paper_id
            analysis.problem_id = problem.problem_id
            totalscore = 0
            if problem.type == 0:
                for answerpaper in answerpapers:
                    totalscore += answerpaper.Answers.filter_by(problem_id = analysis.problem_id).first().score
                    answer = answerpaper.Answers.filter_by(problem_id = analysis.problem_id).first().answer
                    if answer == "T":
                        analysis.T_count += 1
                    elif answer == "F":
                        analysis.F_count += 1
                    else:
                        analysis.NULL_count += 1
            elif problem.type == 1:
                for answerpaper in answerpapers:
                    answer = answerpaper.Answers.filter_by(problem_id = analysis.problem_id).first().answer
                    totalscore += answerpaper.Answers.filter_by(problem_id=analysis.problem_id).first().score
                    if answer == "A":
                        analysis.A_count += 1
                    elif answer == "B":
                        analysis.B_count += 1
                    elif answer == "C":
                        analysis.C_count += 1
                    elif answer == "D":
                        analysis.D_count += 1
                    else:
                        analysis.NULL_count += 1
            else:
                for answerpaper in answerpapers:
                    answer = answerpaper.Answers.filter_by(problem_id = analysis.problem_id).first().answer
                    totalscore += answerpaper.Answers.filter_by(problem_id=analysis.problem_id).first().score
                    if answer.count("A"):
                        analysis.A_count += 1
                    if answer.count("B"):
                        analysis.B_count += 1
                    if answer.count("C"):
                        analysis.C_count += 1
                    if answer.count("D"):
                        analysis.D_count += 1
                    if len(answer) == 0:
                        analysis.NULL_count += 1
            if totalnum == 0:
                analysis.accuracy = 0
            else:
                analysis.accuracy = totalscore / totalnum
            exam.anlsflag = True
            db.session.add(analysis)
            db.session.commit()
    exam = Paper.query.filter_by(paper_id=paper_id).first()
    return render_template('teacher/show_exam.html', exam=exam)








