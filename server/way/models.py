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
    avatar = models.ImageField(upload_to='avatars', blank=True)


class Comment(models.Model):
    content = models.CharField(max_length=200)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    likes = models.IntegerField(default=0)


class PostedImage(models.Model):
    description = models.CharField(max_length=200)
    created = models.DateField()
    likes = models.IntegerField(default=0)
    image = models.ImageField(upload_to='images', blank=True)
