from rest_framework import serializers
from .models import User, Comment, PostedImage, UserStory


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'bio', 'created', 'following', 'avatar')


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('content', 'author', 'likes')


class PostedImageSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = PostedImage
        fields = ('description', 'created', 'likes', 'image', 'author', 'hashtags')

    def get_image(self, obj):
        if obj.image:
            return obj.image.url


class UserStorySerializer(serializers.ModelSerializer):
    class Meta:
        model = UserStory
        fields = ('created', 'author', 'image')
