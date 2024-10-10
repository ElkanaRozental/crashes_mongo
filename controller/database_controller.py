from msilib import init_database

from flask import Blueprint, jsonify

from repository.csv_repository import init_accidents_db
from utils.parse_bson import parse_json

database_blueprint = Blueprint("/initial", __name__)

@database_blueprint.route('/init', methods=['POST'])
def init_data():
    res = init_accidents_db()
    if res:
        return jsonify({
            "message": "data successfully inserted!",
        }), 200
    else:
        return jsonify({"error": "Failed to insert data"}), 500
