from flask import Blueprint


manage_exam_bp = Blueprint('manage_exam', __name__)


@manage_exam_bp.route('/')
def home():
    return '这是教师考试管理的主页面。'
