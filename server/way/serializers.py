from rest_framework import serializers
from .models import User, Comment, PostedImage, UserStory


class UserFollowingSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'avatar')


class UserSerializer(serializers.ModelSerializer):
    followers = UserFollowingSerializer(many=True)
    following = UserFollowingSerializer(many=True)
    class Meta:
        model = User
        fields = ('username', 'bio', 'created', 'following', 'followers', 'avatar')
        depth = 1


class ActionAuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'avatar')


class CommentSerializer(serializers.ModelSerializer):
    author = ActionAuthorSerializer()
    class Meta:
        model = Comment
        fields = ('content', 'author', 'likes')


class PostedImageSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()
    author = ActionAuthorSerializer()
    likes = ActionAuthorSerializer(read_only=True, many=True)

    class Meta:
        model = PostedImage
        fields = ('description', 'created', 'likes', 'image', 'author', 'hashtags')

    def get_image(self, obj):
        if obj.image:
            return obj.image.url


class UserStorySerializer(serializers.ModelSerializer):
    author = ActionAuthorSerializer()
    class Meta:
        model = UserStory
        fields = ('created', 'author', 'image')
