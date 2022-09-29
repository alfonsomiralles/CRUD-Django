from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

class comments(models.Model):
    name = models.CharField(max_length=255, null=False)
    score = models.IntegerField(default=2)
    comment = models.TextField(max_length=1000, null=True)
    date = models.DateField(null=True)
    signature = models.CharField(max_length=100, default="firma")

    def __str__(self):
        return self.name    