from database.connect import daily, weekly, monthly, accidents, areas


def create_indexes():
    daily.create_index({'date': 1, 'area': 1})
    weekly.create_index({'date': 1, 'area': 1})
    monthly.create_index({'date': 1, 'area': 1})
    accidents.create_index({'area': 1})
    areas.create_index({'area': 1})


def execution_stats(area, date):
    return [
        daily.find({'date': date, 'area': area}).hint({'date': 1, 'area': 1}).explain()['executionStats'],
        weekly.find({'date': date, 'area': area}).hint({'date': 1, 'area': 1}).explain()['executionStats'],
        monthly.find({'date': date, 'area': area}).hint({'date': 1, 'area': 1}).explain()['executionStats'],
        accidents.find({'area': area}).hint({'area': 1}).explain()['executionStats'],
        areas.find({'area': area}).hint({'area': 1}).explain()['executionStats']
    ]


def execution_stats_natural(area, date):
    return [
        daily.find({'date': date, 'area': area}).hint({'$natural': 1}).explain()['executionStats'],
        weekly.find({'date': date, 'area': area}).hint({'$natural': 1}).explain()['executionStats'],
        monthly.find({'date': date, 'area': area}).hint({'$natural': 1}).explain()['executionStats'],
        accidents.find({'area': area}).hint({'$natural': 1}).explain()['executionStats'],
        areas.find({'area': area}).hint({'$natural': 1}).explain()['executionStats']
    ]
