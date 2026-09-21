import pytest

from student_result import get_result


@pytest.mark.parametrize(
    "score, attendance, expected",
    [
        (95, 85, "Отлично"),
        (90, 80, "Отлично"),
        (70, 70, "Хорошо"),
        (50, 60, "Зачёт"),
        (49, 100, "Незачёт"),
        (0, 0, "Незачёт"),
    ]
)
def test_get_result(score, attendance, expected):
    assert get_result(score, attendance) == expected


@pytest.mark.parametrize(
    "score, attendance, expected",
    [
        (-1, 80, "Некорректный балл"),
        (101, 80, "Некорректный балл"),
        (80, -1, "Некорректная посещаемость"),
        (80, 101, "Некорректная посещаемость"),
    ]
)
def test_invalid_values(score, attendance, expected):
    assert get_result(score, attendance) == expected


@pytest.mark.parametrize(
    "score, attendance",
    [
        ("90", 80),
        (90, "80"),
        ("abc", 70),
        (70, "abc"),
    ]
)
def test_invalid_type(score, attendance):
    with pytest.raises(TypeError):
        get_result(score, attendance)