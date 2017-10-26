from rest_framework import viewsets


class PersonViewset(viewsets.ModelViewSet):
    @classmethod
    def create_viewset_class(cls, queryset, serialiser_class):
        super()

        cls.queryset = queryset
        cls.serializer_class = serialiser_class

        return cls
