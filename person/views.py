from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status, viewsets


from person.models import Person
from person.serializers import PersonSerializer


class PersonViewSet(viewsets.ModelViewSet):
    serializer_class = PersonSerializer
    queryset = Person.objects.all()
    lookup_field = "name"