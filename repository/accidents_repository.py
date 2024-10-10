from database.connect import accidents


def find_sum_crashes_by_area(area):
    return accidents.count_documents({'area': area})
