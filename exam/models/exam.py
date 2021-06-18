from datetime import datetime

from sqlalchemy import ForeignKey
from exam import db


class Paper(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    subject = db.Column(db.String, nullable=False)
    strt_t = db.Column(db.DateTime, default=datetime.now, nullable=False)
    end_t = db.Column(db.DateTime, nullable=False)
    duration = db.Column(db.DateTime, nullable=False)
    published = db.Column(db.Boolean, nullable=False)
    end = db.Column(db.Boolean, nullable=False)


class exam_has_problem(db.Model):
    exam_id = db.Column(db.Integer, ForeignKey("paper.id"), nullable=False)
    pro_id = db.Column(db.Integer, ForeignKey("problem.problem_id"), nullable=False)






