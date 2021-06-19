from flask import Blueprint


take_exam_bp = Blueprint('take_exam', __name__)


@take_exam_bp.route('/')
def home():
    return '这是学生参加考试的主页面。'


@take_exam_bp.route('/take_exam')
def take_exam():
    return '这是开始考试的界面'


@take_exam_bp.route('/show_exam')
def show_exam():
    return '这是显示答卷的界面'