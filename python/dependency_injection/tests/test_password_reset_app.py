from unittest import mock

from password_reset_app import PasswordResetApp


def test_returns_false_when_passwords_mismatch():
    mock_argument_parser = mock.MagicMock()
    mock_argument_parser.get_password.return_value = 'pwd'
    mock_argument_parser.get_confirmation_password.return_value = 'pwd2'

    app = PasswordResetApp(
        mock.MagicMock(),
        mock_argument_parser,
    )

    assert app.passwords_are_correct() is False


def test_returns_false_when_passwords_match_and_are_not_strong():
    mock_argument_parser = mock.MagicMock()
    mock_argument_parser.get_password.return_value = 'pwd'
    mock_argument_parser.get_confirmation_password.return_value = 'pwd'

    mock_password_strength_evaluator = mock.MagicMock()
    mock_password_strength_evaluator.password_is_strong_enough.return_value = False

    app = PasswordResetApp(
        mock_password_strength_evaluator,
        mock_argument_parser,
    )

    assert app.passwords_are_correct() is False


def test_returns_true_when_passwords_match_and_are_strong():
    mock_argument_parser = mock.MagicMock()
    mock_argument_parser.get_password.return_value = 'pwd'
    mock_argument_parser.get_confirmation_password.return_value = 'pwd'

    mock_password_strength_evaluator = mock.MagicMock()
    mock_password_strength_evaluator.password_is_strong_enough.return_value = True

    app = PasswordResetApp(
        mock_password_strength_evaluator,
        mock_argument_parser,
    )

    assert app.passwords_are_correct() is True
