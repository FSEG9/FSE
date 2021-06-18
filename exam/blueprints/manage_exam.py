from flask import Blueprint, render_template

from exam.forms.exam import generate_exam

manage_exam_bp = Blueprint('manage_exam', __name__)


@manage_exam_bp.route('/')
def home():
    form = generate_exam()
    return render_template('exam_view/gen_exam.html', form=form)


# @manage_exam_bp.route('/add_pro_exam')
# def home():
#     form = generate_exam()
#     return render_template('exam_view/gen_exam.html', form=form)
