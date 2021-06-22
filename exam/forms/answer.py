from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, TextAreaField, HiddenField, RadioField, SubmitField, FieldList,SelectField
from wtforms.validators import ValidationError


def check_has_choice(message=None):
    """验证器：学生不可以不选择"""
    if message is None:
        message = '请选择答案'

    def _check_has_choice(form, field):
        if form.type.data != '0' and (field.data is None or field.data == ''):
            raise ValidationError(message)

    return _check_has_choice


class AnswerForm(FlaskForm):
    problem_id = IntegerField('编号', render_kw={'hidden': ''})
    answer = RadioField('答案', validators=[check_has_choice()])


class PaperForm(FlaskForm):
    answers = FieldList(AnswerForm)