from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create the models
class User(models.Model):
    username = models.CharField(max_length=50)
    bio = models.TextField()
    created = models.DateField()
    following = ArrayField(
        ArrayField(
            models.CharField(max_length=50, blank=True),
        )
    )

class Comment(models.Model):
    content = models.CharField(max_length=200)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )

class Image(models.Model):
    imgURL = models.CharField(max_length=120)
    description = models.CharField(max_length=200)
    created = models.DateField()

