from repository.accidents_repository import find_sum_crashes_by_area


def test_find_sum_crashes_by_area():
    res = find_sum_crashes_by_area('411')
    print(res)
    assert res > 0