from rest_framework import serializers
from .models import User, Comment, PostedImage, UserStory


class UserSerializer(serializers.ModelSerializer):
    avatar = serializers.ImageField(
        max_length=None, use_url=True
    )

    class Meta:
        model = User
        fields = ('username', 'bio', 'created', 'following', 'avatar')


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('content', 'author', 'likes')


class PostedImageSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(
        max_length=None, use_url=True
    )

    class Meta:
        model = PostedImage
        fields = ('description', 'created', 'likes', 'image', 'author', 'hashtags')


class UserStorySerializer(serializers.ModelSerializer):
    class Meta:
        model = UserStory
        fields = ('created', 'author', 'image')
