from rest_framework import serializers

from people.models import Person

__all__ = ['PersonSerialiser']


class PersonSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ('name', 'phone_number')
