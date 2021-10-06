# Custom schema support
from drf_spectacular.utils import extend_schema
from rest_framework import viewsets
from .permissions import IsAdminOrReadOnly
from rest_framework.response import Response
from .models import Profile, Comment, PostedImage, UserStory
from .serializers import ProfileSerializer, CommentSerializer, PostedImageSerializer, UserStorySerializer
from django.contrib.sessions.models import Session
from rest_framework.decorators import action


class ProfileView(viewsets.ModelViewSet):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()
    permission_classes = [IsAdminOrReadOnly]

    @extend_schema(
        request=ProfileSerializer,
        responses=ProfileSerializer,
        description='This route responds with the data of the user signed in with the session id passed in the request.'
    )
    @action(detail=False, methods=['GET'], name='sessionUser')
    def get_session_user(self, request):
        session = Session.objects.get(session_key=request.session.session_key)
        session_data = session.get_decoded()
        uid = session_data.get('_auth_user_id')

        user = Profile.objects.filter(user_id=uid)
        serializer = self.serializer_class(user, many=True)
        return Response(serializer.data)


class CommentView(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()


class PostedImageView(viewsets.ModelViewSet):
    serializer_class = PostedImageSerializer
    queryset = PostedImage.objects.all()
    permission_classes = [IsAdminOrReadOnly]

    @extend_schema(
        request=PostedImageSerializer,
        responses=PostedImageSerializer,
        description='Sometimes we need to get more specific. This route finds all images with a specified hashtag.'
    )
    def get_feed_from_hashtag(self, request, hashtag):
        images = PostedImage.objects.filter(hashtags__icontains=hashtag)
        serializer = self.serializer_class(images, many=True)
        return Response(serializer.data)

    @extend_schema(
        request=PostedImageSerializer,
        responses=PostedImageSerializer,
        description='The feed is a list of all found images that were uploaded by users who the currently logged in user follows.'
    )
    @action(detail=False, methods=['GET'], name='feed')
    def feed(self, request):
        session = Session.objects.get(session_key=request.session.session_key)
        session_data = session.get_decoded()
        uid = session_data.get('_auth_user_id')

        profile = Profile.objects.get(user_id=uid)
        followed = profile.following.values_list('username', flat=True)
        images = PostedImage.objects.filter(author__username__in=followed)
        serializer = self.serializer_class(images, many=True)
        return Response(serializer.data)


class UserStoryView(viewsets.ModelViewSet):
    serializer_class = UserStorySerializer
    queryset = UserStory.objects.all()
    permission_classes = [IsAdminOrReadOnly]

    @extend_schema(
        request=UserStorySerializer,
        responses=UserStorySerializer,
        description='Stories are all groups of images that were uploaded by users who the currently logged in user follows.'
    )
    def get_stories(self, request, username):
        profile = Profile.objects.get(username=username)
        followed = profile.following.values_list('username', flat=True)
        stories = UserStory.objects.filter(author__username__in=followed)
        serializer = self.serializer_class(stories, many=True)
        return Response(serializer.data)
