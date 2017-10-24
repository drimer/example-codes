__all__ = ['PasswordStrengthEvaluator']


class PasswordStrengthEvaluator(object):
    def password_is_strong_enough(self, password: str) -> bool:
        length_valid = self._password_length_is_valid(password)
        has_lowercase = self._password_has_lowercase(password)
        has_uppercase = self._password_has_uppercase(password)
        has_number = self._password_has_number(password)

        return length_valid and has_lowercase and has_uppercase and has_number

    def _password_length_is_valid(self, password: str):
        return len(password) >= 8

    def _password_has_lowercase(self, password: str):
        return password.upper() != password

    def _password_has_uppercase(self, password: str):
        return password.lower() != password

    def _password_has_number(self, password: str):
        return any(ord('1') <= ord(c) <= ord('9') for c in password)
