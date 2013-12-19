from django.contrib.auth.models import User
from django.db import models

class Picture(models.Model):
    uploader = models.ForeignKey(User)
    description = models.CharField(max_length=256)

class Piece(models.Model):
    pictures = models.ManyToManyField(Picture)
