import json
import datetime

my_str = r'C:\Users\manto\PycharmProjects\KR_3\src\operations.json'


def load_operations():
    """функция распаковывающая файл с операциями"""
    with open(my_str, 'r', encoding='utf-8') as file:
        operation = json.load(file)
        return operation


def sort_operation(i):
    """
    функция которая вытаскивает 5 удачных операций в словарь
    :return dict
    """
    last_operatoins = []
    number = 0
    for item in i:
        if number < 5:
            for k, i in item.items():
                if i == 'EXECUTED':
                    last_operatoins.append(item)
                    number += 1

    return last_operatoins


def sort_by_date(i):
    """
    сортирует список по ключу 'date'
    :return dict
    """
    sortid_date = []
    for d in i:
        if d.get('date'):
            sortid_date.append(d)
    sortid_date.sort(key=lambda x: x.get('date'), reverse=True)
    return sortid_date


completed_operations = sort_operation(load_operations())
last_operation = sort_by_date(completed_operations)


def score_from(i):
    """
    функция которая отформатирует счет или карту на которую приходит
    :return: str
    """
    score = i.get("from")
    if score != None:
        score_number = score.split(sep=None, maxsplit=-1)
        score_number = score_number[-1]
        score_type = score.split(sep=None, maxsplit=-1)
        score_type = score_type[0]
    else:
        return ''
    if score_type in 'Счет':
        return f"{score_type} **{score_number[-4:]}"
    else:
        return f"{score_type} {score_number[0:4]} {score_number[4:5]}*** **** {score_number[-4:]}"


def score_to(i):
    """
    функция которая отформатирует счет или карту на которую приходит
    :return: str
    """
    score = i.get("to")
    if score != None:
        score_number = score.split(sep=None, maxsplit=-1)
        score_number = score_number[-1]
        score_type = score.split(sep=None, maxsplit=-1)
        score_type = score_type[0]
    else:
        return ''
    if score_type in 'Счет':
        return f"{score_type} **{score_number[-4:]}"
    else:
        return f"{score_type} {score_number[0:4]} {score_number[4:5]}*** **** {score_number[-4:]}"


def date(i):
    """
    функция которая отформатирует дату
    :return:
    """
    date = datetime.datetime.strptime(i['date'], "%Y-%m-%dT%H:%M:%S.%f").strftime('%d.%m.%Y')
    return date



def name_description(i):
    """
    функция которая отформатирует счет
    :return:
    """
    description = i['description']
    return description


def operationAmount(i):
    """
    функция которая отформатирует счет
    :return:
    """
    amount = i['operationAmount']['amount']
    name_a = i['operationAmount']['currency']['name']
    return f'{amount} {name_a}'
