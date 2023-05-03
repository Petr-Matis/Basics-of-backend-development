import utils.utils
import json


def main():
    """
    Запуск кода для виджета «Операции по счетам»
    """

    with open("operations.json", "r", encoding='UTF-8') as json_file:
        operations = json.load(json_file)
    list_5_operations = utils.utils.list_operations(operations)
    print()
    for operation in list_5_operations:
        print(operation.get_print_operation())
        print()


if __name__ == "__main__":
    main()
