class ObjectiveRepo:
    def create(self, data = {}):
        default_data = {'title': 'New Objective'}
        return {**default_data, **data}
