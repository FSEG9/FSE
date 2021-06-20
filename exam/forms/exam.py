from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, SelectField, IntegerField, DateField, BooleanField
from wtforms.validators import DataRequired, Length


class generate_exam(FlaskForm):
    name = StringField("试卷名称")
    subject = StringField("试卷学科")
    strt_time = StringField("起始时间")
    end_time = StringField("结束时间")
    add_stu = SubmitField("添加学生")
    add_prob = SubmitField("+")
    auto_gen = SubmitField("自动生成试卷")
    submit = SubmitField("提交测试")


class search_add(FlaskForm):
    submit = SubmitField("保存")

