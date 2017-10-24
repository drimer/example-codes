import argparse

__all__ = ['ArgumentParser']


class ArgumentParser(object):
    def __init__(self):
        self._parser = argparse.ArgumentParser()
        self._parser.add_argument('password', type=str)
        self._parser.add_argument('confirmation_password', type=str)

    def get_password(self):
        return self._parser.parse_args().password

    def get_confirmation_password(self):
        return self._parser.parse_args().confirmation_password
