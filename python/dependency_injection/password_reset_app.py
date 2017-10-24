from argument_parser import ArgumentParser
from password_strength_evaluator import PasswordStrengthEvaluator

__all__ = ['PasswordStrengthEvaluator']


class PasswordResetApp(object):
    def __init__(
            self, password_strength_evaluator: PasswordStrengthEvaluator,
            argument_parser: ArgumentParser,
    ):
        self.password_strength_evaluator = password_strength_evaluator
        self.argument_parser = argument_parser

    def passwords_are_correct(self) -> bool:
        password = self.argument_parser.get_password()
        confirmation_password = self.argument_parser.get_confirmation_password()

        is_strong = self.password_strength_evaluator.password_is_strong_enough(password)
        return password == confirmation_password and is_strong
