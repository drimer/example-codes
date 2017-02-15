import hashlib
import uuid
from functools import wraps

from flask import request, jsonify

SHORT_URL_DOMAIN = 'be.ri'
MAX_SHORTURL_LENGTH = 23


def generate_shorturl(full_url):
    """
    Genearates a shorturl given a `full_url`.

    :param full_url: URL to shorten
    :return: Shortened version of the url
    """
    salt = '{}{}'.format(full_url, uuid.uuid4())
    _hash = hashlib.md5(salt.encode('utf-8')).hexdigest()
    result = '{}/{}'.format(SHORT_URL_DOMAIN, _hash)

    return result[:MAX_SHORTURL_LENGTH]


def with_schema(schema):
    """
    Decorator for routes that deserializes json data using a schema,
    and passes to the view in the json_data parameter.
    """

    def _dec(f):
        @wraps(f)
        def wrapped(*args, **kw):
            json = request.json
            if not json:
                return jsonify({
                    'message': 'Json data not received',
                }), 400
            json_data, errors = schema().load(json)
            if errors:
                return jsonify({
                    'message': 'BadRequest',
                    'errors': errors,
                }), 400
            return f(json_data=json_data, *args, **kw)

        return wrapped

    return _dec
