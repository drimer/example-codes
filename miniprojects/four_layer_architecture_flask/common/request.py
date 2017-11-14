from flask.globals import request
from werkzeug.exceptions import BadRequest


class Request(object):
    POST = 'POST'
    GET = 'GET'

    def get_json(self) -> dict:
        if self.is_json():
            try:
                json = request.json
            except BadRequest:
                json = {}
        else:
            json = request.json

        return json

    def method_is(self, method: str) -> bool:
        return request.method == method

    def is_json(self) -> bool:
        return request.headers.get('Content-Type') == 'application/json'
