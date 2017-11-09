from flask.globals import request


class Request(object):
    def get_json(self):
        return request.json
