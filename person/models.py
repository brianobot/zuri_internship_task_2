from django.db import models
import uuid
from django.utils.translation import gettext_lazy as _


def generate_id(length: int = 10):
    return uuid.uuid4().hex[:length]


class BaseModelMixin(models.Model):
    id = models.CharField(primary_key=True, default=generate_id, editable=False, max_length=255)
    uid = models.CharField(default=generate_id, editable=False, max_length=255)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False, db_index=True)
    active = models.BooleanField(_("active"), default=True, db_index=True)

    class Meta:
        abstract = True


class Person(BaseModelMixin):
    name = models.CharField(max_length=100, blank=False, null=False)

    def __str__(self) -> str:
        return self.name
