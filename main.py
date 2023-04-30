from utils.utils import load_operations, list_operations


def main():
    """
    Запуск кода для виджета «Операции по счетам»
    """
    url_operations = "https://api.jsonserve.com/eb3AO5"
    list_5_operations = list_operations(load_operations(url_operations))
    print()
    for operation in list_5_operations:
        print(operation.get_print_operation())
        print()

if __name__ == "__main__":
    main()