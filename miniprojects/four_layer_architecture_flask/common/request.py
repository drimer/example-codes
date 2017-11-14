from flask.globals import request


class Request(object):
    POST = 'POST'
    GET = 'GET'

    def get_json(self) -> object:
        return request.json

    def method_is(self, method: str) -> bool:
        return request.method == method

    def is_json(self) -> bool:
        return request.headers.get('Content-Type') == 'application/json'
