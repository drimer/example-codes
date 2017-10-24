import sys

from dependency_injection.container import DIContainer

if __name__ == '__main__':
    app = DIContainer.password_reset_app()
    are_correct = app.passwords_are_correct()

    if are_correct:
        print('Passwords are correct.')
        sys.exit(0)
    else:
        print('Passwords seem wrong.')
        sys.exit(-1)
