from database.connect import areas, daily


def group_cause_by_area(area):
    return areas.aggregate(
        [
            {
                '$match': {'area': area}
            },
            {
                '$group': {
                    '_id': '$prim_contributory_cause',
                    'total_accidents': {'$sum': '$sum_accident'},
                    'total_injuries': {'$sum': '$injuries.total'},
                    'total_fatal': {'$sum': '$injuries.fatal'},
                    'total_incapacitating': {'$sum': '$injuries.incapacitating'},
                    'total_non_incapacitating': {'$sum': '$injuries.non_incapacitating'}

                }
            }
        ]
    ).to_list()

def get_statistics(area):
    pipeline = [
        {
            '$match': {'area': area}},
        {
            '$group': {
                '_id': None,
                'total_injuries': {'$sum': {'$toInt': '$injuries.total'}},
                'total_fatal': {'$sum': {'$toInt': '$injuries.fatal'}},
                'total_non_fatal': {
                    '$sum': {
                        '$subtract': [
                            {'$toInt': '$injuries.total'},
                            {'$toInt': '$injuries.fatal'}
                        ]
                    }
                }
            }
        }
    ]
    return areas.aggregate(pipeline).to_list()

print(get_statistics('1650'))