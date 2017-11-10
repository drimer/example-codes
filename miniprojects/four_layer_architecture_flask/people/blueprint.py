from flask.blueprints import Blueprint

from people.presentation.views import PeopleListOrCreateView


class BlueprintFactory(object):
    @staticmethod
    def create():
        blueprint = Blueprint('people', 'people')

        blueprint.add_url_rule(
            '/person',
            view_func=PeopleListOrCreateView.as_view('people-list-or-create'),
        )

        return blueprint
