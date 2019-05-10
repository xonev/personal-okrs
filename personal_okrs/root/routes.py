from flask import Blueprint, jsonify, request
from personal_okrs.core.objective_service import ObjectiveService
from personal_okrs.core.objective_repo import ObjectiveRepo

root = Blueprint('root', __name__)

objective_repo = ObjectiveRepo()


def build_objective_service():
    return ObjectiveService(objective_repo)


@root.route("/", methods=['GET'])
def status_index():
    return jsonify({
        'name': "Personal OKRs",
        'version': '0.0.0-alpha'
    })


@root.route("/objectives", methods=['POST'])
def objectives_create():
    objective_service = build_objective_service()

    objective = objective_service.create(request.get_json())

    return jsonify(objective)


@root.route("/objectives/<int:objective_id>", methods=['GET'])
def objectives_get(objective_id):
    objective_service = build_objective_service()

    objective = objective_service.get(objective_id)

    return jsonify(objective)


@root.route("/objectives", methods=['GET'])
def objectives_index():
    objective_service = build_objective_service()

    objectives = objective_service.list()

    return jsonify(objectives)


