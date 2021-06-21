from datetime import datetime

from sqlalchemy import ForeignKey
from exam import db
from exam.models.answer import exam_has_anspaper

exam_has_problem = db.Table(
    'exam_has_problem',
    db.Column('problem_id', db.Integer, db.ForeignKey('problem.problem_id')),
    db.Column('paper_id', db.Integer, db.ForeignKey('paper.paper_id'))
)


class Paper(db.Model):
    name = db.Column(db.String(50), nullable=True)
    paper_id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(40), nullable=True)
    strt_t = db.Column(db.DateTime, default=datetime.now, nullable=True)
    end_t = db.Column(db.DateTime, nullable=True)
    end = db.Column(db.Boolean,  default=False)
    score = db.Column(db.Float, default=-1)
    problems = db.relationship('Problem',
                               secondary=exam_has_problem,
                               back_populates='papers')
    anspapers = db.relationship('Anspaper')
    