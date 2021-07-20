from django.db import models
from django.contrib.postgres.fields import ArrayField


class User(models.Model):
    username = models.CharField(max_length=50)
    bio = models.TextField()
    created = models.DateField()
    following = models.ManyToManyField('self', blank=True, related_name='followedby', symmetrical=False)
    avatar = models.ImageField(upload_to='avatars', blank=True, null=True)

    @property
    def followers(self):
        return self.followedby.all()


class Comment(models.Model):
    content = models.CharField(max_length=200)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    likes = models.ManyToManyField(User, blank=True, related_name='liked_comments', symmetrical=False)


class PostedImage(models.Model):
    description = models.CharField(max_length=200)
    created = models.DateField()
    likes = models.ManyToManyField(User, blank=True, related_name='liked_images', symmetrical=False)
    hashtags = ArrayField(
            models.CharField(max_length=50),
            null=True,
            blank=True
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    image = models.ImageField(upload_to='images', blank=True, null=True)
    comments = models.ForeignKey(
        Comment,
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )


class UserStory(models.Model):
    created = models.DateField()
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    image = models.ImageField(upload_to='stories', blank=True, null=True)
