from flask.json import jsonify


class JsonViewMixin:
    """
    When sub-classing this mixin, it's required that a request attribute exists,
    and that it should be an instance of common.request.Request.
    """

    def dispatch_request(self, *args, **kwargs):
        if not self.request.is_json():
            return jsonify({
                'message': 'Invalid request. Make sure your content type is application/json',
            }), 415

        return super().dispatch_request(*args, **kwargs)
