import json
import arrow
import datetime


my_str = r'C:\Users\manto\PycharmProjects\KR_3\src\operations.json'


def load_operations():
    """функция распаковывающая файл с операциями"""
    with open(my_str, 'r', encoding='utf-8') as file:
        return json.load(file)



def sort_operation(i):
    """
    функция которая вытаскивает 5 удачных операций в словарь

    """
    last_operatoins = []
    number = 0
    for item in i:
        for k, i in item.items():
            if i == 'EXECUTED':
                last_operatoins.append(item)
    return last_operatoins

def sort_by_date(i):
    """
    сортирует список по ключу 'date'

    """
    sortid_date = []
    for d in i:
        if d.get('date'):
            sortid_date.append(d)
    sortid_date.sort(key=lambda x: x.get('date'), reverse=True)
    return sortid_date

