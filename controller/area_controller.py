from flask import Blueprint, jsonify

from repository.area_repository import group_cause_by_area, get_statistics
from utils.parse_bson import parse_json

area_blueprint = Blueprint("/area", __name__)

@area_blueprint.route('/<area>', methods=['GET'])
def get_group_cause_by_area(area):
    res = group_cause_by_area(area)
    if res:
        return jsonify({
            "message": "data successfully pulled!",
            "data": parse_json(res)
        }), 200
    else:
        return jsonify({"error": "Failed to pull data"}), 500

@area_blueprint.route('/statistics/<area>', methods=['GET'])
def get_stat(area):
    res = get_statistics(area)
    if res:
        return jsonify({
            "message": "data successfully pulled!",
            "data": parse_json(res)
        }), 200
    else:
        return jsonify({"error": "Failed to pull data"}), 500


