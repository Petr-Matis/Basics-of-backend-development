from operation.operation import *


def data_masking(disguise: str | None):
    """
    Маскировка данных карт в формате XXXX XX** **** XXXX и счетов в формате **XXXX
    :param disguise: str данные
    :return: str маскированные данные
    """
    if disguise is None:
        return None
    if disguise[-20:].isdigit():
        return disguise[-len(disguise):-20] + '**' + disguise[-4:]
    if disguise[-16:].isdigit():
        return disguise[-len(disguise):-16] + disguise[-16:-12] + " " + disguise[-12:-10] + "** **** " + disguise[-4:]


def list_operations(json_transactions):
    """
    Загрузка операций в класс и предоставления списка из 5-и последних операций
    :param json_transactions: JSON всех транзакций
    :return: List 5-и последних транзакций
    """
    if json_transactions is None:
        raise NameError(f"Список пуст {type(json_transactions)}")
    list_transactions = []
    for transaction in json_transactions:
        if transaction == {}:
            continue
        if transaction.setdefault('state') in [None, "CANCELED"]:
            continue
        dt_transaction = dt.strptime(transaction.setdefault('date'), "%Y-%m-%dT%H:%M:%S.%f")
        add_transaction = Operation(id=transaction.setdefault('id'),
                                    state=transaction.setdefault('state'),
                                    date=dt_transaction,
                                    amount=transaction['operationAmount'].setdefault('amount'),
                                    name=transaction['operationAmount']['currency'].setdefault('name'),
                                    code=transaction['operationAmount']['currency'].setdefault('code'),
                                    description=transaction.setdefault('description'),
                                    from_=data_masking(transaction.setdefault('from')),
                                    to=data_masking(transaction.setdefault('to'))
                                    )
        if len(list_transactions) == 0:
            list_transactions.append(add_transaction)
            continue
        for x in range(len(list_transactions)):
            dt_list_transaction = list_transactions[x].get_date()
            if dt_transaction > dt_list_transaction:
                list_transactions.insert(x, add_transaction)
                break
            elif dt_transaction < dt_list_transaction and x + 1 == len(list_transactions):
                list_transactions.append(add_transaction)
            elif dt_transaction < dt_list_transaction:
                continue
        if len(list_transactions) > 5:
            list_transactions.pop()
    return list_transactions
