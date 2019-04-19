from personal_okrs.core.objective_repo import ObjectiveRepo


def test_create():
    repo = ObjectiveRepo()
    assert repo.create() == {'title': 'New Objective'}

def test_create_with_data():
    repo = ObjectiveRepo()
    assert repo.create({'description': 'Really good objective'}) == \
        {'title': 'New Objective', 'description': 'Really good objective'}
