from rest_framework import serializers
from .models import User, Comment, PostedImage


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'bio', 'created', 'following')


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('content', 'author')


class PostedImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostedImage
        fields = ('imgURL', 'description', 'created')
