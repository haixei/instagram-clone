# Custom schema support
from django.contrib.auth.decorators import login_required
from drf_spectacular.utils import extend_schema, OpenApiParameter
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Profile, Comment, PostedImage, UserStory
from .serializers import ProfileSerializer, CommentSerializer, PostedImageSerializer, UserStorySerializer


class ProfileView(viewsets.ModelViewSet):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()


class CommentView(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()


class PostedImageView(viewsets.ModelViewSet):
    serializer_class = PostedImageSerializer
    queryset = PostedImage.objects.all()

    @extend_schema(
        request=PostedImageSerializer,
        responses=PostedImageSerializer,
    )
    def get_feed(self, request, username):
        print('test')
        profile = Profile.objects.get(username=username)
        followed = profile.following.values_list('username', flat=True)
        images = PostedImage.objects.filter(author__username__in=followed)
        serializer = self.serializer_class(images, many=True)
        return Response(serializer.data)

    @extend_schema(
        request=PostedImageSerializer,
        responses=PostedImageSerializer,
    )
    def get_feed_from_hashtag(self, request, hashtag):
        images = PostedImage.objects.filter(hashtags__icontains=hashtag)
        serializer = self.serializer_class(images, many=True)
        return Response(serializer.data)


class UserStoryView(viewsets.ModelViewSet):
    serializer_class = UserStorySerializer
    queryset = UserStory.objects.all()

    @extend_schema(
        request=UserStorySerializer,
        responses=UserStorySerializer,
    )
    def get_stories(self, request, username):
        profile = Profile.objects.get(username=username)
        followed = profile.following.values_list('username', flat=True)
        stories = UserStory.objects.filter(author__username__in=followed)
        serializer = self.serializer_class(stories, many=True)
        return Response(serializer.data)
