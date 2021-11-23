from datetime import datetime
from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone


class Profile(models.Model):
    username = models.CharField(max_length=50, default='', unique=True)
    bio = models.TextField(max_length=100, blank=True, default='')
    created = models.DateField(default=timezone.now(), blank=True)
    following = models.ManyToManyField('self', blank=True, related_name='followedby', symmetrical=False)
    avatar = models.ImageField(upload_to='avatars', blank=True, null=True, default="default.jpg")
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    @property
    def followers(self):
        return self.followedby.all()

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            username = 'user' + str(instance.id)
            Profile.objects.create(user=instance, username=username)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()


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
    seen_by = models.ManyToManyField(User, blank=True, related_name='seen_stories', symmetrical=False)
