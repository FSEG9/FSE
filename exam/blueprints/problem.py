from flask import Blueprint


problem_bp = Blueprint('problem', __name__)


@problem_bp.route('/')
def home():
    return '这是教师题库管理的主页面。'
