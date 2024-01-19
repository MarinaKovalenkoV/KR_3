import datetime
from function import load_operations, sort_operation, sort_by_date


def main():

    operation = load_operations()
    completed_operations = sort_operation(operation)
    last_operation = sort_by_date(completed_operations)

    numeber = 0
    for i in last_operation:
        if i.get('from'):
            """счет откуда пришел платеж"""
            score = i['from']
            score_number = score.split()[-1]
            score_type = (score.split()[0])
            """счет куда пришел платеж"""
            score_to = i['to']
            score_to_number = score_to.split()[-1]
            score_to_type = (score_to.split()[0])
            """дата"""
            date = datetime.datetime.strptime(i['date'], "%Y-%m-%dT%H:%M:%S.%f").strftime('%d.%m.%Y')
            """описание операции"""
            description = i['description']
            """сумма перевода"""
            amount = i['operationAmount']['amount']
            """валюта"""
            currency = i['operationAmount']['currency']['name']
            print(f"{date} {description}")
            print(f"{score_type} {score_number[0:4]} {score_number[4:5]}** **** {score_number[-4:]} -> {score_to_type} **{score_to_number[-4:]}")
            print(f"{amount} {currency}\n")
            numeber += 1
            if numeber == 5:
                break

main()