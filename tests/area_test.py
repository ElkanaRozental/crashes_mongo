import pytest

from repository.area_repository import group_cause_by_area


def test_group_cause_by_area():
    res = group_cause_by_area('1235')
    print(res)
    assert len(res) > 0