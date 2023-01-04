import pytest

from easy_test.utils import get_verbal_grade

grade_parameters = [
    (2, "Плохо"),
    (3, "Удовлетворительно"),
    (4, "Хорошо"),
    (5, "Отлично"),
]


@pytest.mark.parametrize("grade_int, grade_str", grade_parameters)
def test_get_verbal_grade(grade_int, grade_str):
    assert get_verbal_grade(grade_int) == grade_str


grade_exceptions = [
    (1, ValueError),
    (6, ValueError),
    ("5", TypeError),
    (5.0, TypeError),
]


@pytest.mark.parametrize("grade_int, exception", grade_exceptions)
def test_get_verbal_grade_exceptions(grade_int, exception):
    with pytest.raises(exception):
        assert get_verbal_grade(grade_int)

# или когда нужно только одну проверку сделать
# def test_get_verbal_grade_value_error_l():
#     with pytest.raises(ValueError):
#         assert get_verbal_grade(1)