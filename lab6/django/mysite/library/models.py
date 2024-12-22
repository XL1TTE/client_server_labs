
from django.db import models


class Book(models.Model):
    id = models.IntegerField(primary_key=True, null=False)
    title = models.CharField(max_length=55, null=False)
    author = models.CharField(max_length=55, null=True)


