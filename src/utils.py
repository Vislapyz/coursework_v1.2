import json


def data_operations(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        data = json.load(file)
        return data