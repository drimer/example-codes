from datetime import datetime

from flask import Blueprint
from flask import jsonify, Flask

from models import Person, db
from schemas import PersonSchema
from utils import with_schema

person_blueprint = Blueprint('person', 'person')


@person_blueprint.route('/person/', methods=['POST'])
@with_schema(PersonSchema)
def post_person(json_data):
    first_name = json_data['first_name']
    phone_number = json_data['phone_number']

    qry = Person.query.filter_by(phone_number=phone_number)
    if qry.count():
        entity = qry.first()
        return jsonify(PersonSchema().dump(entity).data)

    entity = Person(
        first_name=first_name,
        phone_number=phone_number,
        created=datetime.utcnow(),
    )

    db.session.add(entity)
    db.session.commit()

    return jsonify(PersonSchema().dump(entity).data)


@person_blueprint.route('/person/<int:id>', methods=['GET'])
def get_person(id):
    qry = Person.query.filter_by(id=id)
    if qry.count() == 0:
        return jsonify({'message': 'Url not found'}), 404

    entity = qry.first()

    db.session.add(entity)
    db.session.commit()

    return jsonify(PersonSchema().dump(entity).data)


def create_app():
    api = Flask('api')
    api.register_blueprint(person_blueprint)
    db.init_app(api)

    with api.app_context():
        db.create_all()

    return api


app = create_app()
