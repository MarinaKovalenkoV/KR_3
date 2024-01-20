from function import load_operations, sort_operation, sort_by_date, date, name_description, score_from, score_to, operationAmount

completed_operations = sort_operation(load_operations())
last_operation = sort_by_date(completed_operations)

def main():
    for i in last_operation:
        print(f'{date(i)} {name_description(i)}')
        print(f'{score_from(i)} -> {score_to(i)}')
        print(f'{operationAmount(i)}')

main()
