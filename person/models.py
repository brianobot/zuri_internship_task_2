from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    
    def __str__(self) -> str:
        return self.name
    
    