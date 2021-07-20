# Custom schema support
from drf_spectacular.utils import extend_schema, OpenApiParameter
from rest_framework import viewsets
from rest_framework.response import Response
from .models import User, Comment, PostedImage, UserStory
from .serializers import UserSerializer, CommentSerializer, PostedImageSerializer, UserStorySerializer


class UserView(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    # Show how the response will look like in the documentation
    @extend_schema(
        request=UserSerializer,
        responses=UserSerializer,
    )
    # Define a custom route
    def get_user_by_username(self, request, username):
        user = User.objects.get(username=username)
        print(user.followedby.all())
        serializer = self.serializer_class(user)
        return Response(serializer.data)


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
        user = User.objects.get(username=username)
        followed = user.following.values_list('username', flat=True)
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
        user = User.objects.get(username=username)
        followed = user.following.values_list('username', flat=True)
        stories = UserStory.objects.filter(author__username__in=followed)
        serializer = self.serializer_class(stories, many=True)
        return Response(serializer.data)
