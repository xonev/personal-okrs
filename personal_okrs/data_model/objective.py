from personal_okrs import db

class Objective(db.Model):
    id = db.Column(db.String(255), primary_key=True)
    goal_id = db.Column(db.String(255), db.ForeignKey('goal.id'), nullable=False)
    goal = db.relationship('Goal', lazy=True, uselist=False)