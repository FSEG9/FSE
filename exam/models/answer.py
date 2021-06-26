from exam import db
from datetime import datetime

exam_has_anspaper = db.Table(
    'exam_has_anspaper',
    db.Column('paper_id', db.Integer, db.ForeignKey('paper.paper_id')),
    db.Column('anspaper_id', db.Integer, db.ForeignKey('anspaper.anspaper_id'))
)


class Anspaper(db.Model):
    anspaper_id = db.Column(db.Integer, nullable=False, primary_key=True)
    paper_id = db.Column(db.Integer, db.ForeignKey('paper.paper_id',ondelete='CASCADE'))
    student_id = db.Column(db.Integer)
    score_all = db.Column(db.Integer)
    Ranknum = db.Column(db.Integer, default=0)
    Answers = db.relationship("Anspa_prob_answer", lazy='dynamic')

class Anspa_prob_answer(db.Model):
    anspaper_id = db.Column(db.Integer, db.ForeignKey('anspaper.anspaper_id',ondelete='CASCADE'), nullable=False, primary_key=True)
    problem_id = db.Column(db.Integer, db.ForeignKey('problem.problem_id',), nullable=False, primary_key=True)
    answer = db.Column(db.String(5))
    score = db.Column(db.Integer)

# class exam_has_probanls(db.Model):

class ProbAnalysis(db.Model):
    exam_id = db.Column(db.Integer, db.ForeignKey('paper.paper_id',ondelete='CASCADE'), nullable=False, primary_key=True)
    problem_id = db.Column(db.Integer, db.ForeignKey('problem.problem_id'), nullable=False, primary_key=True)
    A_count = db.Column(db.Integer, default=0)
    B_count = db.Column(db.Integer, default=0)
    C_count = db.Column(db.Integer, default=0)
    D_count = db.Column(db.Integer, default=0)
    T_count = db.Column(db.Integer, default=0)
    F_count = db.Column(db.Integer, default=0)
    NULL_count = db.Column(db.Integer, default=0)
    accuracy = db.Column(db.Float)
    problem = db.relationship('Problem')
