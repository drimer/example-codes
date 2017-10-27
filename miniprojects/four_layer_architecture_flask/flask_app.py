from flask import Flask


def create_app(db, blueprints):
    api = Flask('api')

    for blueprint in blueprints:
        api.register_blueprint(blueprint)

    db.init_app(api)

    with api.app_context():
        db.create_all()

    return api
