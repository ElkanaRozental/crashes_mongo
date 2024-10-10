import csv
import os
from database.connect import daily, weekly, monthly, areas, reasons, accidents
from utils.data_utils import convert_to_date,get_week_range,get_month_range,convert_to_int


def read_csv(csv_path):
   with open(csv_path, 'r') as file:
       csv_reader = csv.DictReader(file)
       for row in csv_reader:
           yield row

def init_accidents_db():
    # if accidents.count_documents({}) > 0:
    #     return

    daily.drop()
    weekly.drop()
    monthly.drop()
    areas.drop()
    reasons.drop()
    accidents.drop()

    data_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'short_data.csv')
    for row in read_csv(data_path):

        converted_to_date = convert_to_date(row['CRASH_DATE'])

        accident = {
            'crash_date': converted_to_date,
            'area': row['BEAT_OF_OCCURRENCE'],
            'injuries': {
                'total': row['INJURIES_TOTAL'],
                'fatal': row['INJURIES_FATAL'],
                'incapacitating': row['INJURIES_INCAPACITATING'],
                'non_incapacitating': row['INJURIES_NON_INCAPACITATING']
            },
            'cause': {
                'prim_contributory_cause': row['PRIM_CONTRIBUTORY_CAUSE'],
                'set_contributory_cause': row['SEC_CONTRIBUTORY_CAUSE']
            }
        }

        accidents.insert_one(accident)

        # day = {
        #     # 'date': start_week,
        #     # 'beat_of_occurrence': row['BEAT_OF_OCCURRENCE'],
        #     'crash_id': row['CRASH_RECORD_ID'],
        # }

        daily.update_one(
            {'date': convert_to_date(row['CRASH_DATE']),
             'area': row['BEAT_OF_OCCURRENCE']},
            {
             '$inc': {'sum_accident': 1}
             },
            upsert=True
        )

        start_week = get_week_range(converted_to_date)[0]
        end_week = get_week_range(converted_to_date)[1]

        # week = {
        #    # 'start_week': start_week,
        #    # 'end_week': end_week,
        #    # 'beat_of_occurrence': row['BEAT_OF_OCCURRENCE'],
        #    'crash_id': row['CRASH_RECORD_ID'],
        # }

        weekly.update_one(
           { 'start_week': start_week, 'end_week': end_week,
             'area': row['BEAT_OF_OCCURRENCE'] },
           {
             '$inc': {'sum_accident': 1}
             },
           upsert=True
        )

        convert_to_month = get_month_range(converted_to_date)[0]
        convert_to_year = get_month_range(converted_to_date)[1]

        # month = {
        #    # 'month': start_week,
        #    # 'year': end_week,
        #    # 'beat_of_occurrence': row['BEAT_OF_OCCURRENCE'],
        #    'crash_id': row['CRASH_RECORD_ID'],
        # }

        monthly.update_one(
           { 'month': convert_to_month, 'year': convert_to_year,
             'area': row['BEAT_OF_OCCURRENCE'], },
           {
             '$inc': { 'sum_accident': 1 }
           },

           upsert=True
        )

        # accident_area = {
        #     'beat_of_occurrence': row['BEAT_OF_OCCURRENCE'],
        #     'prim_contributory_cause': row['PRIM_CONTRIBUTORY_CAUSE'],
        # }

        areas.update_one(
            {
                'area': row['BEAT_OF_OCCURRENCE'],
                'prim_contributory_cause': row['PRIM_CONTRIBUTORY_CAUSE'],
            },
            {
                '$inc': {
                    'sum_accident': 1,
                    'injuries.total': convert_to_int(row['INJURIES_TOTAL']),
                    'injuries.fatal': convert_to_int(row['INJURIES_FATAL']),
                    'injuries.incapacitating': convert_to_int(row['INJURIES_INCAPACITATING']),
                    'injuries.non_incapacitating': convert_to_int(row['INJURIES_NON_INCAPACITATING']),
                },
                '$push': {'crash_id': row['CRASH_RECORD_ID']}
            },
            upsert=True
        )


