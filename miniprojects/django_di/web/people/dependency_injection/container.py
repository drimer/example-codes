from dependency_injector import providers

from people.models import Person
from people.serialisers import PersonSerialiser
from people.views import PersonViewset


class DIContainer(object):
    person_view_set = providers.Callable(
        PersonViewset.create_viewset_class,
        Person.objects.all(),
        PersonSerialiser
    )
