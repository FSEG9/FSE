from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, HiddenField, SelectField, SubmitField, IntegerField
from wtforms.validators import ValidationError


def text_not_empty(message=None):
    """验证器：非空"""
    if message is None:
        message = '必须输入题干。'

    def _text_not_empty(form, field):
        if field.data is None or field.data == '':
            raise ValidationError(message)

    return _text_not_empty


def check_has_choice(message=None):
    """验证器：若为单选或多选，选项不能为空"""
    if message is None:
        message = '选择题必须输入 4 个选项。'

    def _check_has_choice(form, field):
        if form.type.data != '0' and (field.data is None or field.data == ''):
            raise ValidationError(message)

    return _check_has_choice


def check_solution(message=None):
    """验证器：答案必须为 T/F/A/B/C/D/AB/BC/CD/AC/BD/AD/ABC/ABD/ACD/BCD/ABCD"""

    def _check_solution(form, field):
        if form.type.data == '0' and field.data not in ['T', 'F']:
            raise ValidationError('判断题答案必须为 T 或 F。')
        if form.type.data == '1' and field.data not in ['A', 'B', 'C', 'D']:
            raise ValidationError('单选题答案必须为 A、B、C 或 D。')
        if form.type.data == '2' and field.data not in ['A', 'B', 'C', 'D', 'AB', 'BC', 'CD', 'AC',
                                                        'BD', 'AD', 'ABC', 'ABD', 'ACD', 'BCD', 'ABCD']:
            raise ValidationError('多选题答案必须为 ABCD 的非空组合。')

    return _check_solution


class ProblemForm(FlaskForm):
    problem_id = IntegerField('编号', render_kw={'hidden': ''})
    type = SelectField('题目类型', choices=[('0', '判断'), ('1', '单选'), ('2', '多选')])
    text = TextAreaField('题干', validators=[text_not_empty()])
    choice_A = StringField('选项 A', validators=[check_has_choice()])
    choice_B = StringField('选项 B', validators=[check_has_choice()])
    choice_C = StringField('选项 C', validators=[check_has_choice()])
    choice_D = StringField('选项 D', validators=[check_has_choice()])
    solution = StringField('答案', validators=[check_solution()])
    adder = HiddenField('添加人', default='Default User')  # TODO: 添加登录验证
    tags = StringField('标签（多个标签用空格分隔）')
    submit = SubmitField('添加试题')
