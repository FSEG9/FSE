from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, SelectField, IntegerField, DateField, BooleanField
from wtforms.validators import DataRequired, Length


class generate_exam(FlaskForm):
    strt_time = StringField("起始时间")
    end_time = StringField("结束时间")
    submit = SubmitField("添加学生")
    submit = SubmitField("+")
    submit = SubmitField("自动生成试卷")
    submit = SubmitField("保存测试")


