import pytest

from repository.area_repository import group_cause_by_area, get_statistics


def test_group_cause_by_area():
    res = group_cause_by_area('1235')
    print(res)
    assert len(res) > 0


def test_statistics_by_area():
    res = get_statistics('411')
    print(res)
    assert len(res) > 0