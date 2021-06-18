from flask import Blueprint


view_exam_bp = Blueprint('view_exam', __name__)


@view_exam_bp.route('/')
def home():
    return '这是学生考试信息查看的主页面。'
