from flask import Blueprint, jsonify

root = Blueprint('root', __name__)


@root.route("/", methods=['GET'])
def feed_index():
    return jsonify({
        'name': "Personal OKRs",
        'version': '0.0.0-alpha'
    })
