from function.function import sort_operation, sort_by_date

test_list = [
    {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041"
    }, {
        "id": 27192367,
        "state": "CANCELED",
        "date": "2018-12-24T20:16:18.819037"
    }, {
        "id": 667307132,
        "state": "EXECUTED",
        "date": "2019-07-13T18:51:29.313309"
    }, {
        "id": 957763565,
        "state": "EXECUTED",
        "date": "2019-01-05T00:52:30.108534"
    }, {
        "id": 207126257,
        "state": "EXECUTED",
        "date": "2019-07-15T11:47:40.496961"
    }, {
        "id": 921286598,
        "state": "EXECUTED",
        "date": "2018-03-09T23:57:37.537412"
    }
]

def test_sort_operations():
    """
    тестируем фукнцию по вытаскиванию 5 удачных операций
    """
    assert sort_operation(test_list) == [
        {
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041"
        }, {
            "id": 667307132,
            "state": "EXECUTED",
            "date": "2019-07-13T18:51:29.313309"
        }, {
            "id": 957763565,
            "state": "EXECUTED",
            "date": "2019-01-05T00:52:30.108534"
        }, {
            "id": 207126257,
            "state": "EXECUTED",
            "date": "2019-07-15T11:47:40.496961"
        }, {
            "id": 921286598,
            "state": "EXECUTED",
            "date": "2018-03-09T23:57:37.537412"
        }
    ]

def test_sort_by_date():
    """
    тестируем фукнцию по сортировки 'date'
    """
    assert sort_by_date(test_list) == [
        {
            'id': 441945886,
            'state': 'EXECUTED',
            'date': '2019-08-26T10:50:58.294041'
        }, {
            'id': 207126257,
            'state': 'EXECUTED',
            'date': '2019-07-15T11:47:40.496961'
        }, {
            'id': 667307132,
            'state': 'EXECUTED',
            'date': '2019-07-13T18:51:29.313309'
        }, {
            'id': 957763565,
            'state': 'EXECUTED',
            'date': '2019-01-05T00:52:30.108534'
        }, {
            'id': 27192367,
            'state': 'CANCELED',
            'date': '2018-12-24T20:16:18.819037'
        }, {
            'id': 921286598,
            'state': 'EXECUTED',
            'date': '2018-03-09T23:57:37.537412'
        }
    ]