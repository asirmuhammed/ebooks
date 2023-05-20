from django.db import models
from versatileimagefield.fields import VersatileImageField, PPOIField
from tinymce.models import HTMLField

# Create your models here.


class Book(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)

    def __str__(self):
        return self.title