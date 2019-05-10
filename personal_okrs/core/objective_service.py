from personal_okrs.core.objective_repo import ObjectiveRepo


class ObjectiveService(object):
    def __init__(self, objective_repo: ObjectiveRepo):
        self.objective_repo = objective_repo

    def list(self):
        return self.objective_repo.list()

    def create(self, attributes):
        # validation
        default_data = {'title': 'New Objective'}

        objective_data = {**default_data, **attributes}

        return self.objective_repo.create(objective_data)

    def get(self, objective_id):
        return None

    def delete(self, objective_id):
        pass

    def update(self, attributes):
        pass