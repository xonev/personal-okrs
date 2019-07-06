import uuid
from personal_okrs import db
from personal_okrs.data_model.objective import Objective
from personal_okrs.data_model.goal import Goal

    # id = db.Column(db.String(255), primary_key=True)
    # title = db.Column(db.String(512))
    # description = db.Column(db.Text())
    # type = db.Column(db.Enum(GoalType))
    # direction_of_progress = db.Column(db.Enum(ProgressDirection))
    # due_date = db.Column(db.DateTime())
    # current_value = db.Column(db.Numeric())
    # start_value = db.Column(db.Numeric())

class ObjectiveRepo(object):
    def __init__(self):
        pass


    def create(self, data):
        goal_id = uuid.uuid4()
        objective_id = uuid.uuid4()

        goal = Goal(
            id=goal_id,
            title=data['title'],
            description = data['description'],
            type = data['type'],
            direction_of_progress = data['direction_of_progress'],
            due_date = data['due_date'],
            current_value = data['current_value'],
            start_value = data['start_value']
        )

        objective = Objective(
            id=objective_id,
            goal=goal
        )

        db.session.add(objective)
        db.session.commit()

        return objective.dict()


    def list(self):
        return self.objectives
