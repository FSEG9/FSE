from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, HiddenField, RadioField, SubmitField, FieldList,SelectField

problemtext = "这是一个卑微的题干"

class ProblemForm(FlaskForm):
    text = StringField(problemtext)
    #submit = SubmitField('提交')
    judgechoices = RadioField(choices=[('正确'), ('错误')])
    singlechoices = RadioField(choices=[('A:', '这是选项A'), ('B:', '这是选项B'), ('C:', '这是选项C'), ('D:', '这是选项D')])
    multichoices = RadioField(choices=[('A:', '判断'), ('B:', '单选'), ('C:', '多选'), ('D:', '多选')])
    #多选题要改