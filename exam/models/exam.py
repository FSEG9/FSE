from sqlalchemy import ForeignKey
from exam import db


class Paper(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String)
    strt_t = db.Column(db.DateTime)
    end_t = db.Column(db.DateTime)
    duration = db.Column(db.DateTime)
    published = db.Column(db.Boolean)
    end = db.Column(db.Boolean)


class exam_has_problem(db.Model):
    exam_id = db.Column(db.Integer, ForeignKey("paper.id"))
    pro_id = db.Column(db.Integer, ForeignKey("problem.problem_id"))






