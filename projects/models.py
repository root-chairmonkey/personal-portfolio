from django.db import models
from django.db.models.enums import Choices
from django.utils import timezone

# Create your models here.


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=20)
    collaborator = models.CharField(null=True,max_length=100)
    comment = models.TextField(null=True, blank=True)
    date_created = models.DateTimeField(default=timezone.now)
    status = models.CharField(null=True, max_length=100)

    def __str__(self):
        return self.title
    