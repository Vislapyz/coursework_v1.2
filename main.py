from src.utils import data_operations, date_conversions, operations_from_the_list, data_task_condition


def main():
    global operation
    filename = 'operations.json'
    operations_sorted = operations_from_the_list(data_operations(filename))

    last_five_operations = operations_sorted[0:5]

    for operation in last_five_operations:
        date = date_conversions(operation['date'])
        print(f"{date} {operation['description']}")

        # Создание условия для вывода данных по операциям, у которых отсутвует ключ "from" и с ключом
        if 'from' not in operation:
            num_from = "Открытие вклада"
        else:
            num_from = data_task_condition(operation['from'])
        num_to = data_task_condition(operation['to'])
        print(f"{num_from} -> {num_to}")
        print(f"{operation['operationAmount']['amount']} {operation['operationAmount']['currency']['name']}")
        print()


if __name__ == "__main__":
    main()
