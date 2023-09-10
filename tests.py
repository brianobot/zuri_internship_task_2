import pytest
import requests
from django.urls import reverse

from person.models import Person


def test_list_persons():
    url = reverse("persons:person-list")
    response = requests.get(url)
    assert response.status_code == 200


def test_create_person():
    url = reverse("person:person-list")
    data = {
        'name': "Brian David Obot"
    }
    response = requests.post(url, data)
    assert response.status_code == 201


def test_person_detail():
    james = Person.objects.create(name="James")
    url = reverse("persons:person-detail", args=("James"))
    response = requests.get(url)
    assert response.status_code == 200


def test_update_person():
    james = Person.objects.create(name="James")
    url = reverse("persons:person-detail", args=("James"))
    response = requests.get(url)
    assert response.status_code == 200


def test_delete_person():
    james = Person.objects.create(name="James")
    url = reverse("persons:person-detail", args=("James"))
    response = requests.get(url)
    assert response.status_code == 204

    


