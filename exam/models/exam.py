from datetime import datetime

from exam import db

exam_has_problem = db.Table(
    'exam_has_problem',
    db.Column('problem_id', db.Integer, db.ForeignKey('problem.problem_id')),
    db.Column('paper_id', db.Integer, db.ForeignKey('paper.paper_id'))
)


class Paper(db.Model):
    name = db.Column(db.String(50), nullable=False)
    paper_id = db.Column(db.Integer, primary_key=True, nullable=False)
    subject = db.Column(db.String(40), nullable=False)
    strt_t = db.Column(db.DateTime, default=datetime.now, nullable=False)
    end_t = db.Column(db.DateTime, nullable=False)
    end = db.Column(db.Boolean, nullable=False, default=False)
    problems = db.relationship('Problem',
                               secondary=exam_has_problem,
                               back_populates='papers')
