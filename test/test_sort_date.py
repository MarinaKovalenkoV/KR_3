from function.function import sort_by_date, date

test_list = [
    {
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
    }, {
        "state": "CANCELED",
        "date": "2018-12-24T20:16:18.819037"
    }, {
        "state": "EXECUTED",
        "date": "2019-07-13T18:51:29.313309"
    }, {
        "state": "EXECUTED",
        "date": "2019-01-05T00:52:30.108534"
    }, {
        "state": "EXECUTED",
        "date": "2019-07-15T11:47:40.496961"
    }, {
        "state": "EXECUTED",
        "date": "2018-03-09T23:57:37.537412"
    }
]

test_list_d = {"date": "2019-08-26T10:50:58.294041"}
test_list_d_1 = {"date": "2018-12-24T20:16:18.819037"}

def test_sort_by_date():
    """
    тестируем фукнцию по сортировки 'date'
    """
    assert sort_by_date(test_list) == [
        {
            'state': 'EXECUTED',
            'date': '2019-08-26T10:50:58.294041'
        }, {
            'state': 'EXECUTED',
            'date': '2019-07-15T11:47:40.496961'
        }, {
            'state': 'EXECUTED',
            'date': '2019-07-13T18:51:29.313309'
        }, {
            'state': 'EXECUTED',
            'date': '2019-01-05T00:52:30.108534'
        }, {
            'state': 'CANCELED',
            'date': '2018-12-24T20:16:18.819037'
        }, {
            'state': 'EXECUTED',
            'date': '2018-03-09T23:57:37.537412'
        }
    ]

def test_date():
    assert date(test_list_d) == "26.08.2019"
    assert date(test_list_d_1) == "24.12.2018"