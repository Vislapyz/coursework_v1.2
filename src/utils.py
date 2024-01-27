import json


def data_operations(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        data = json.load(file)
        return data


def operations_from_the_list(data):
    state_executed = []
    for operation in data:
        if 'state' in operation and  operation['state'] == 'EXECUTED':
            state_executed.append(operation)

    operation_sorted = sorted(state_executed, key=lambda x: x['date'], reverse=True)
    return operation_sorted