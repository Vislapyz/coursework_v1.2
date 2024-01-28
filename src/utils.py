import json


def data_operations(filename: str):
    with open(filename, 'r', encoding='utf-8') as file:
        data = json.load(file)
        return data


def operations_from_the_list(data: list):
    state_executed = []
    for operation in data:
        if 'state' in operation and operation['state'] == 'EXECUTED':
            state_executed.append(operation)

    operation_sorted = sorted(state_executed, key=lambda x: x['date'], reverse=True)
    return operation_sorted


def date_conversions(date: str):
    date = date.split('T')[0].split('-')
    return f'{date[2]}.{date[1]}.{date[0]}'


def data_task_condition(data_number: str):
    if "Счет" in data_number:
        num_chek = data_number.split(' ')[1]
        name_chek = data_number.split(' ')[0]
        return f"{name_chek} ** {num_chek[-4:]}"

    elif "Visa" in data_number:
        num_cart = data_number.split(' ')[-1]
        name_cart = data_number.split(' ')[0:-1]
        full_name_cart = " ".join(name_cart)
        return f"{full_name_cart} {num_cart[0:4]} {num_cart[5:7]}** **** {num_cart[-4:]}"

    else:
        num_cart = data_number.split(' ')[1]
        name_cart = data_number.split(' ')[0]
        return f"{name_cart} {num_cart[0:4]} {num_cart[5:7]}** **** {num_cart[-4:]}"
