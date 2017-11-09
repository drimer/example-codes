from flask.blueprints import Blueprint

from people.presentation.views import create_person, get_person


class BlueprintFactory(object):
    @staticmethod
    def create():
        blueprint = Blueprint('people', 'people')

        blueprint.add_url_rule('/person', view_func=create_person, methods=['POST'])
        blueprint.add_url_rule('/person/<int:pk>', view_func=get_person, methods=['GET'])

        return blueprint
