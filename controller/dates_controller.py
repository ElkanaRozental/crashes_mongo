from flask import Blueprint, jsonify

from repository.date_repository import find_sum_crashes_by_area_and_date
from utils.parse_bson import parse_json

date_blueprint = Blueprint("/date", __name__)

@date_blueprint.route('/<area>/<date>', methods=['GET'])
def get_crashes_by_area_and_date(area, date):
    res = find_sum_crashes_by_area_and_date(area, date)
    if res:
        return jsonify({
            "message": "data successfully pulled!",
            "data": parse_json(res)
        }), 200
    else:
        return jsonify({"error": "Failed to pull data"}), 500