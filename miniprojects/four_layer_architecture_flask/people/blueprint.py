from flask.blueprints import Blueprint

from .views import create_person


class BlueprintFactory(object):
    @staticmethod
    def create():
        blueprint = Blueprint('people', 'people')

        blueprint.route('/person/', methods=['POST'])(create_person)

        return blueprint
