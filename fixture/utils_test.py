from utils import sum_func


def test_sum_func(two_numbers_sum):  # обратите внимание на имя
    sum_result = sum_func(two_numbers_sum[0], two_numbers_sum[1])
    assert sum_result == two_numbers_sum[2]
