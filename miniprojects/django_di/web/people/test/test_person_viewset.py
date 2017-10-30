from unittest import mock
from unittest.case import TestCase

from rest_framework.serializers import Serializer, ModelSerializer

from people.views import PersonViewset


class MockSerialiser(Serializer):
    def __init__(self, *args, **kwargs):
        super()

        self.data = 'serialized'


class TestPersonViewset(TestCase):
    def setUp(self):
        self.mock_queryset = mock.MagicMock()
        self.mock_serialiser = mock.MagicMock()
        self.mock_serialiser_class = MockSerialiser
        self.mock_request = mock.MagicMock()

    def test_that_get_person_list_returns_all(self):
        self.mock_queryset.objects.all.return_value = []
        self.mock_serialiser.data = 'serialised'

        view_class = PersonViewset.create_viewset_class(
            self.mock_queryset,
            self.mock_serialiser_class,
        )
        view = view_class(request=self.mock_request, format_kwarg=None)

        response = view.list(self.mock_request)
        import ipdb; ipdb.set_trace()
        pass