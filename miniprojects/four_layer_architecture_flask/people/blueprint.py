from flask.blueprints import Blueprint

from .views import create_person


class BlueprintFactory(object):
    @staticmethod
    def create():
        blueprint = Blueprint('people', 'people')

        blueprint.add_url_rule('/person', view_func=create_person, methods=['POST'])

        return blueprint
