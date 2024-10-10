from datetime import datetime

from database.connect import daily
from utils.data_utils import convert_to_date


def find_sum_crashes_by_area_and_date(area, date):
    date = datetime.strptime(date, '%Y-%m-%d')
    res = daily.find({
        'area': area,
        'date': {
            '$gte': datetime(date.year, date.month, date.day),
            '$lt': datetime(date.year, date.month, date.day + 1)
        }
    })
    total_accidents = 0
    for result in res:
        total_accidents += result.get('sum_accident', 0)

    return total_accidents

