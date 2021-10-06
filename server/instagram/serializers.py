from rest_framework import serializers
from .models import Profile, Comment, PostedImage, UserStory


class ProfileFollowingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'


class ProfileSerializer(serializers.ModelSerializer):
    followers = ProfileFollowingSerializer(many=True)
    following = ProfileFollowingSerializer(many=True)

    class Meta:
        model = Profile
        fields = '__all__'
        depth = 1


class ActionAuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    author = ActionAuthorSerializer()

    class Meta:
        model = Comment
        fields = '__all__'


class PostedImageSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()
    author = ActionAuthorSerializer()
    likes = ActionAuthorSerializer(read_only=True, many=True)

    class Meta:
        model = PostedImage
        fields = '__all__'

    def get_image(self, obj):
        if obj.image:
            return obj.image.url


class UserStorySerializer(serializers.ModelSerializer):
    author = ActionAuthorSerializer()
    seen = ActionAuthorSerializer(read_only=True, many=True)

    class Meta:
        model = UserStory
        fields = '__all__'
