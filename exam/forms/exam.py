from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, SelectField, IntegerField, DateField, BooleanField
from wtforms.validators import DataRequired, Length


class generate_exam(FlaskForm):
    name = StringField("试卷名称")
    subject = StringField("试卷学科")
    start_time = StringField()
    start_date = StringField()
    end_time = StringField()
    end_date = StringField()
    auto_gen = SubmitField("自动生成试卷")
    submit = SubmitField("发布测试")


class search_add(FlaskForm):
    submit = SubmitField("保存")

