from django.urls import path, include
from rest_framework.routers import DefaultRouter

from person import views

app_name = "persons"


router = DefaultRouter()
router.register(r"api", views.PersonViewSet, basename="person")


urlpatterns = [
    path("", include(router.urls)),
]
