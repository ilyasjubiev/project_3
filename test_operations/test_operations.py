from utils.utils import get_date, unpacking_data, filtered_data, get_last_values, get_from_or_to, get_list_of_operations


def test_unpacking_data():
    data = unpacking_data()
    assert isinstance(data, list)

def test_filtered_data():
    assert filtered_data({}) == []
    assert filtered_data("123434567") == []
    assert filtered_data([{"state": "EXECUTED"}, {"state": "CANCELED"}]) == [{'state': 'EXECUTED'}]

def test_get_last_values(test_data):
    data = get_last_values(test_data, 3)
    assert [x['date'] for x in data] == ['2019-07-03T18:35:29.512364', '2019-04-04T23:20:05.206878',
                                         '2019-03-23T01:09:46.296404']


def test_get_date():
    data = "2019-08-26T10:50:58.294041"
    assert get_date(data) == "26.08.2019"

def test_get_from_or_to():
    data = "Maestro 1596837868705199"
    assert get_from_or_to(data) == 'Maestro **9683'
    data = "Счет 64686473678894779589"
    assert get_from_or_to(data) == 'Счет 6468 64** **** 9589'

def test_get_list_of_operations(test_data):
    assert get_list_of_operations(test_data) == ['03.07.2019 Перевод организации '
                                                 '\nMasterCard **5830 Счет 3538 30** **** 5560 '
                                                 '\n8221.37 USD', '30.06.2018 Перевод организации '
                                                                  '\nСчет 7510 68** **** 6952 Счет 1177 66** **** 6702 '
                                                                  '\n9824.07 USD', '23.03.2018 Открытие вклада '
                                                                                   '\n Счет 4142 15** **** 2431 '
                                                                                   '\n48223.05 руб.',
                                                 '04.04.2019 Перевод со счета на счет '
                                                 '\nСчет 1970 86** **** 8542 Счет 7565 16** **** 4188 '
                                                 '\n79114.93 USD', '23.03.2019 Перевод со счета на счет '
                                                                   '\nСчет 4481 22** **** 4719 '
                                                                   'Счет 7448 96** **** 1160 '
                                                                   '\n43318.34 руб.']