import pytest

from password_strength_evaluator import PasswordStrengthEvaluator


@pytest.mark.parametrize("password,expected", [
    ("Short1", False),
    ('ONLYUPPERCASE', False),
    ('onlylowercase', False),
    ('WithoutNumber', False),
    ('ReallyLongAndValid1', True),
])
def test_password_strength_is_correctly_calculated(password, expected):
    pwd_evaluator = PasswordStrengthEvaluator()
    is_strong = pwd_evaluator.password_is_strong_enough(password)

    assert is_strong == expected
