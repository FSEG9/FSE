from flask import Blueprint


take_exam_bp = Blueprint('take_exam', __name__)


@take_exam_bp.route('/')
def home():
    return '这是学生参加考试的主页面。'
