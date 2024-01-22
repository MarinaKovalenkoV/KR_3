from src.function import load_operations, sort_operation, sort_by_date, date, name_description, score_from, score_to, operationAmount


def main():
    for i in sort_by_date(sort_operation(load_operations())):
        print(f'{date(i)} {name_description(i)}')
        print(f'{score_from(i)} -> {score_to(i)}')
        print(f'{operationAmount(i)}')

main()
