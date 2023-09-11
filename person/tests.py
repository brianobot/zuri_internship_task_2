import pytest
import requests
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework.response import Response

from person.models import Person


@pytest.fixture
def client():
    return APIClient()


@pytest.mark.django_db
def test_list_persons(client: APIClient):
    url = reverse("persons:person-list")
    response: Response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_create_person(client: APIClient):
    url = reverse("persons:person-list")
    data = {
        'name': "Brian David Obot"
    }
    response: Response = client.post(url, data)
    assert response.status_code == 201


@pytest.mark.django_db
def test_person_detail(client: APIClient):
    james = Person.objects.create(name="James")
    url = reverse("persons:person-detail", args=(james.pk,))
    response: Response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_update_person(client: APIClient):
    jame = Person.objects.create(name="James")
    url = reverse("persons:person-detail", args=(jame.pk,))
    response: Response = client.put(url, data={"name": "Jamie"})
    jame.refresh_from_db()
    assert response.status_code == 200
    assert jame.name == "Jamie"


@pytest.mark.django_db
def test_delete_person(client: APIClient):
    james = Person.objects.create(name="James")
    url = reverse("persons:person-detail", args=(james.pk,))
    response: Response = client.delete(url)
    assert response.status_code == 204
