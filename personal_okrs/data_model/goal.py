from personal_okrs import db
import enum


class GoalType(enum.Enum):
    binary = 'binary'
    number = 'number'
    percent = 'percent'


class ProgressDirection(enum.Enum):
    positive = 'positive'
    negative = 'negative'


class Goal(db.Model):
    id = db.Column(db.String(255), primary_key=True)
    title = db.Column(db.String(512))
    description = db.Column(db.Text())
    type = db.Column(db.Enum(GoalType))
    direction_of_progress = db.Column(db.Enum(ProgressDirection))
    due_date = db.Column(db.DateTime())
    current_value = db.Column(db.Numeric())
    start_value = db.Column(db.Numeric())
