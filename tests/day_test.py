from repository.day_repository import find_sum_crashes_by_area_and_date


def test_find_sum_crashes_by_area_and_date():
    res = find_sum_crashes_by_area_and_date('411', '2023-09-22')
    print(res)
    assert res > 0