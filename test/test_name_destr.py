from src.function import name_description, operationAmount

test_list = {
    "id": 596171168,
    "state": "EXECUTED",
    "date": "2018-07-11T02:26:18.671407",
    "operationAmount": {
      "amount": "79931.03",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Открытие вклада",
    "to": "Счет 72082042523231456215"
  }
test_list_1 = {
    "id": 716496732,
    "state": "EXECUTED",
    "date": "2018-04-04T17:33:34.701093",
    "operationAmount": {
      "amount": "40701.91",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Перевод организации",
    "from": "Visa Gold 5999414228426353",
    "to": "Счет 72731966109147704472"
  }


def test_name_description():
    assert name_description(test_list) ==  "Открытие вклада"
    assert name_description(test_list_1) == "Перевод организации"

def test_operationAmount():
    assert operationAmount(test_list_1) == "40701.91 USD"
    assert operationAmount(test_list) == "79931.03 руб."