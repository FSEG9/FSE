from flask import Flask, render_template_string
from flask_sqlalchemy import SQLAlchemy

import pymysql
pymysql.install_as_MySQLdb()
app = Flask('exam')
app.config.from_pyfile('settings.py')

db = SQLAlchemy(app)


@app.route('/')
def main():
    return render_template_string('''
<a href="{{ url_for('problem.home') }}">教师题目管理</a><br />   
<a href="{{ url_for('manage_exam.home') }}">教师考试管理</a><br />
<a href="{{ url_for('view_exam.home') }}">学生考试查看</a><br />
<a href="{{ url_for('teacher.home') }}">老师查看考试</a><br />
''')


from exam.commands import initdb, forge_problems
from exam.blueprints.problem import problem_bp
from exam.blueprints.manage_exam import manage_exam_bp
from exam.blueprints.view_exam import view_exam_bp
from exam.blueprints.take_exam import take_exam_bp
from exam.blueprints.teacher import teacher_bp

app.register_blueprint(problem_bp, url_prefix='/problem')
app.register_blueprint(manage_exam_bp, url_prefix='/manage_exam')
app.register_blueprint(view_exam_bp, url_prefix='/view_exam')
app.register_blueprint(take_exam_bp, url_prefix='/take_exam')
app.register_blueprint(teacher_bp, url_prefix='/teacher_result')