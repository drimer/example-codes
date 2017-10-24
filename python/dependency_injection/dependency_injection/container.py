from dependency_injector import providers

from argument_parser import ArgumentParser
from password_reset_app import PasswordResetApp
from password_strength_evaluator import PasswordStrengthEvaluator


class DIContainer(object):
    argument_parser = providers.Factory(
        ArgumentParser
    )

    password_strength_evaluator = providers.Factory(
        PasswordStrengthEvaluator
    )

    password_reset_app = providers.Singleton(
        PasswordResetApp,
        password_strength_evaluator,
        argument_parser,
    )
