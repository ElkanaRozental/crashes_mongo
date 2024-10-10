from datetime import timedelta, datetime


def convert_to_date(date_string):
    date_format = "%m/%d/%Y"
    return datetime.strptime(date_string.split()[0], date_format)


def get_week_range(date):
    start = date - timedelta(days=date.weekday())
    end = start + timedelta(days=6)
    return [start, end]


def get_month_range(date):
    return [date.month, date.year]


def convert_to_int(value):
        if value == '':
            return 0
        return int(value)