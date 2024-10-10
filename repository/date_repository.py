from datetime import datetime

from database.connect import daily, weekly
from utils.data_utils import convert_to_date, get_week_range


def find_sum_crashes_by_area_and_date(area, date):
    date = datetime.strptime(date, '%Y-%m-%d')
    res = daily.find({
        'area': str(area),
        'date': {
            '$gte': datetime(date.year, date.month, date.day),
            '$lt': datetime(date.year, date.month, date.day + 1)
        }
    })
    total_accidents = 0
    for result in res:
        total_accidents += result.get('sum_accident', 0)

    return total_accidents

def find_sum_crashes_by_area_and_week(area, date):
    date = datetime.strptime(date, '%Y-%m-%d')
    start_date = get_week_range(date)[1]
    end_date = get_week_range(date)[0]
    weekly.aggregate([{
        '$match': {
            'area': str(area),
            'start_week': {'$eq': start_date},
            'end_week': {'$eq': end_date}
        }
    },
    {
        '$group': {
            '_id': None,
            'total_accidents': {'$sum': '$sum_accident'}
        }
    }
    ]).to_list()

