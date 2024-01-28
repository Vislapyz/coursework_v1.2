from src.utils import data_operations, operations_from_the_list, date_conversions, data_task_condition


def test_data_operations():
    """
    Получение из json данные
    """
    assert len(data_operations('operations.json')) > 0


def test_operations_from_the_list(test_fixture):
    """
     Проверка сортировки
    """
    assert len(operations_from_the_list(test_fixture)) == 5
    assert operations_from_the_list(test_fixture)[0]['date'] == "2019-01-26T15:40:13.413061"
    assert operations_from_the_list(test_fixture)[3]['date'] == "2018-04-04T17:33:34.701093"


def test_date_conversions(test_fixture):
    """
    Проверка что дата выводиться в нужном формате
    """
    assert date_conversions(operations_from_the_list(test_fixture)[0]['date']) == '26.01.2019'
    assert date_conversions(operations_from_the_list(test_fixture)[3]['date']) == '04.04.2018'


def test_data_task_condition(test_fixture):
    """
    Проверка вывода номера счета или карты
    """
    assert data_task_condition(operations_from_the_list(test_fixture)[2]['from']) == 'Счет ** 8655'
    assert data_task_condition(operations_from_the_list(test_fixture)[3]['from']) == 'Visa Gold 5999 14** **** 6353'
    assert data_task_condition(operations_from_the_list(test_fixture)[0]['from']) == 'Maestro 4598 00** **** 4501'