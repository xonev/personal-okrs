import uuid


class ObjectiveRepo(object):
    def __init__(self):
        self.objectives = []

    def create(self, data):
        data['id'] = uuid.uuid4()

        self.objectives.append(data)

        return data

    def list(self):
        return self.objectives
