
from flask import Blueprint, jsonify

from repository.csv_repository import init_accidents_db
from repository.idexing_repository import create_indexes, execution_stats, execution_stats_natural
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
        return jsonify({"error": "Failed or finish to insert data"}), 500

@database_blueprint.route('/index', methods=['POST'])
def index_data():
    res = create_indexes()
    if res:
        return jsonify({
            "message": "data successfully indexed!",
        }), 200
    else:
        return jsonify({"error": "Failed or finish to indexing data"}), 500

@database_blueprint.route('/explain/<area>/<date>', methods=['GET'])
def execution_stats_data(area, date):
    res = execution_stats(area, date)
    if res:
        return jsonify({
            "message": "explain successfully!",
            'data': parse_json(res)
        }), 200
    else:
        return jsonify({"error": "Failed to explain stats"}), 500

@database_blueprint.route('/explain_natural/<area>/<date>', methods=['GET'])
def execution_stats_natural_data(area, date):
    res = execution_stats_natural(area, date)
    if res:
        return jsonify({
            "message": "explain successfully!",
            'data': parse_json(res)
        }), 200
    else:
        return jsonify({"error": "Failed to explain stats"}), 500