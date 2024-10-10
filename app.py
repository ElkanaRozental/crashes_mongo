from flask import Flask

from controller.area_controller import area_blueprint
from controller.database_controller import database_blueprint
from controller.dates_controller import date_blueprint
from repository.csv_repository import init_accidents_db

app = Flask(__name__)

if __name__ == '__main__':
    app.register_blueprint(database_blueprint, url_prefix="/api/initial")
    app.register_blueprint(area_blueprint, url_prefix="/api/area")
    app.register_blueprint(date_blueprint, url_prefix="/api/date")
    app.run(debug=True)