from flask.app import Flask

from dependency_injection.container import DIContainer

if __name__ == '__main__':
    app = DIContainer.create_app()
    app.run()
