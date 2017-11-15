from flask.json import jsonify
from marshmallow.schema import Schema


class JsonSerialiser(object):
    def serialise(self, schema: Schema, person, many=None) -> str:
        return jsonify(schema.dump(person, many=many).data)
