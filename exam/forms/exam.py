from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, SelectField, IntegerField, DateField, BooleanField
from wtforms.validators import DataRequired, Length


def check_has_number(message=None):
    """验证器：若为单选或多选，选项不能为空"""
    if message is None:
        message = '请选择题目数量'

    def _check_has_num(form, field):
        if form.type.data != '0' and (field.data is None or field.data == ''):
            raise ValidationError(message)

    return _check_has_choice


class generate_exam(FlaskForm):
    name = StringField("试卷名称")
    subject = StringField("试卷学科")
    start_time = StringField()
    start_date = StringField()
    end_time = StringField()
    end_date = StringField()
    condition = SubmitField()
    submit = SubmitField("发布测试")
    chosenTag = StringField()
    num_problem = IntegerField()



class search_add(FlaskForm):
    submit = SubmitField("保存")

