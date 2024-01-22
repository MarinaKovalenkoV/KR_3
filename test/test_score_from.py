from src.function import score_from, score_to

test_list_date = {"from": "Maestro 1596837868705199"}
test_list_date_1 = {"from": "Счет 75106830613657916952"}
test_list_date_4 = {}
test_list_date_2 = {"to": "Счет 35383033474447895560"}
test_list_date_3 = {"to": "Visa Platinum 8990922113665229"}



def test_score_from():
    assert score_from(test_list_date) == 'Maestro 1596 8*** **** 5199'
    assert score_from(test_list_date_1) == 'Счет **6952'
    assert score_from(test_list_date_4) == ''


def test_score_to():
    assert score_to(test_list_date_2) == 'Счет **5560'
    assert score_to(test_list_date_3) == 'Visa 8990 9*** **** 5229'
    assert score_to(test_list_date_4) == ''