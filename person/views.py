from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status, viewsets


from person.models import Person
from person.serializers import PersonSerializer


class PersonViewSet(viewsets.ModelViewSet):
    serializer_class = PersonSerializer
    queryset = Person.objects.all()

    def destroy(self, request, *args, **kwargs):
        instance: Person = self.get_object()
        instance_id = instance.pk
        self.perform_destroy(instance)
        return Response(
            {"message": f"Person with id '{instance_id}' has been deleted"},
            status=status.HTTP_204_NO_CONTENT,
        )
