import hw_1
import pytest

def test_nearest_number_1():
    str_1 = '-1 -3 -5 -7 -9'  # Последовательность
    str_2 = '1 3 5 7 9'
    str_3 = '7'
    str_4 = '2 4 6 8 10'

    num_1 = -4                # Целевое число
    num_2 = 4
    num_3 = 7
    num_4 = 5

    result_1 = -5
    result_2 = 3
    result_3 = 7
    result_4 = 4

    assert result_1 == hw_1.check_nearest_number(str_1, num_1)
    assert result_2 == hw_1.check_nearest_number(str_2, num_2)
    assert result_3 == hw_1.check_nearest_number(str_3, num_3)
    assert result_4 == hw_1.check_nearest_number(str_4, num_4)


def test_text_exam():
    str_1 = 'hello world hello universe'
    str_2 = ''
    str_3 = 'apple apple apple apple apple'

    result_1 = 3
    result_2 = 0
    result_3 = 1

    assert result_1 == hw_1.text_exam(str_1)
    assert result_2 == hw_1.text_exam(str_2)
    assert result_3 == hw_1.text_exam(str_3)

def test_count_customers():
    lst_1 = ['14.11.1990', '17.02.2021', '16.08.2010']
    lst_2 = []
    lst_3 = ['14.11.1990']

    result_1 = 2
    result_2 = 0
    result_3 = 1

    assert result_1 == hw_1.count_customers(lst_1)
    assert result_2 == hw_1.count_customers(lst_2)
    assert result_3 == hw_1.count_customers(lst_3)

