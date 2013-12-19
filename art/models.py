from django.contrib.auth.models import User
from django.db import models

from taggit.managers import TaggableManager

class Picture(models.Model):
    uploader = models.ForeignKey(User)

class Piece(models.Model):
    description = models.CharField(max_length=256)
    pictures = models.ManyToManyField(Picture)
    tags = TaggableManager()

    # location: geo
