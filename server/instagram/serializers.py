from rest_framework import serializers
from .models import Profile, Comment, PostedImage, UserStory

# Fields that should be visible to anyone who fetches user profile in a public mode
public_access_fields = ('username', 'bio', 'following', 'avatar')


class ProfileFollowingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = public_access_fields


class ProfilePublicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = public_access_fields
        depth = 1


class ProfileSerializer(serializers.ModelSerializer):
    followers = ProfileFollowingSerializer(many=True)
    following = ProfileFollowingSerializer(many=True)

    class Meta:
        model = Profile
        fields = '__all__'
        depth = 1


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class PostedImageSerializer(serializers.ModelSerializer):
    likes = ProfileSerializer(read_only=True, many=True)

    class Meta:
        model = PostedImage
        fields = '__all__'


class UserStorySerializer(serializers.ModelSerializer):
    seen = ProfileSerializer(read_only=True, many=True)

    class Meta:
        model = UserStory
        fields = '__all__'
