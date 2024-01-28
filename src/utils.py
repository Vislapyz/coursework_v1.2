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


def data_task_condition(data_number):
    if 'Счет'in data_number:
        n_account = data_number.slit(' ')[1]
        name_account = data_number.split(' ')[0]
        return  f'{n_account} ** {name_account[-4:]}'
    elif 'Visa' in data_number:
        card_number = data_number.split(' ')[-1]
        card_name = data_number.split(' ')[0:-1]
        full_the_card = ' '.json(card_name)
        return f'{full_the_card} {card_number[0:4]} {card_number[5:7]}** **** {card_number[-4:]}'
    else:
        card_number = data_number.split(' ')[1]
        card_name = data_number.split(' ')[0]
        return f'{card_name} {card_number[0:4] } {card_number[5:7]}** **** {card_number[-4:]}'