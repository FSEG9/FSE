from exam import db
from datetime import datetime

exam_has_anspaper = db.Table(
    'exam_has_anspaper',
    db.Column('paper_id', db.Integer, db.ForeignKey('paper.paper_id')),
    db.Column('anspaper_id', db.Integer, db.ForeignKey('anspaper.anspaper_id'))
)


class Anspaper(db.Model):
    anspaper_id = db.Column(db.Integer, nullable=False, primary_key=True)
    paper_id = db.Column(db.Integer, nullable=False)
    student_id = db.Column(db.Integer, nullable=False)
    start_t = db.Column(db.DateTime, default=datetime.now, nullable=False)
    end_t = db.Column(db.DateTime)
    score_all = db.Column(db.Integer)
    Answers = db.relationship("Anspa_prob_answer")
    paper = db.relationship('Paper',
                            secondary=exam_has_anspaper,
                            back_populates='anspapers')


class Anspa_prob_answer(db.Model):
    anspaper_id = db.Column(db.Integer, db.ForeignKey('anspaper.anspaper_id'), nullable=False, primary_key=True)
    problem_id = db.Column(db.Integer, db.ForeignKey('problem.problem_id'), nullable=False, primary_key=True)
    answer = db.Column(db.String(5))
    problems = db.relationship('Problem')