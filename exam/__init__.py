from flask import Flask, render_template_string
from flask_sqlalchemy import SQLAlchemy


app = Flask('exam')
app.config.from_pyfile('settings.py')

db = SQLAlchemy(app)


@app.route('/')
def main():
    return render_template_string('''
<a href="{{ url_for('problem.home') }}">教师题目管理</a><br />   
<a href="{{ url_for('manage_exam.home') }}">教师考试管理</a><br />
<a href="{{ url_for('view_exam.home') }}">学生考试查看</a><br />
<a href="{{ url_for('take_exam.home') }}">学生参与考试</a><br />  
''')


from exam.commands import initdb
from exam.blueprints.problem import problem_bp
from exam.blueprints.manage_exam import manage_exam_bp
from exam.blueprints.view_exam import view_exam_bp
from exam.blueprints.take_exam import take_exam_bp

app.register_blueprint(problem_bp, url_prefix='/problem')
app.register_blueprint(manage_exam_bp, url_prefix='/manage-exam')
app.register_blueprint(view_exam_bp, url_prefix='/view-exam')
app.register_blueprint(take_exam_bp, url_prefix='/take-exam')