from src.utils import data_operations, operations_from_the_list, date_conversions, data_task_condition


def test_data_operations():
    assert len(data_operations('operations.json')) > 0


def test_operations_from_the_list(test_fixture):
    assert len(operations_from_the_list(test_fixture)) == 5
    assert operations_from_the_list(test_fixture)[0]['date'] == "2424-12-13T22:46:21.935582"

def test_date_conversions(test_fixture):
    assert date_conversions(operations_from_the_list(test_fixture))[0]['date'] == '13.12.2424'