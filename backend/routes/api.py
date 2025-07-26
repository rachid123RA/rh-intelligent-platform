from flask import Blueprint, jsonify

api_blueprint = Blueprint('api', __name__)

@api_blueprint.route("/ping")
def ping():
    return jsonify({"message": "pong"})
