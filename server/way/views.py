# Custom schema support
from drf_spectacular.utils import extend_schema
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Profile, Comment, PostedImage, UserStory
from .serializers import ProfileSerializer, CommentSerializer, PostedImageSerializer, UserStorySerializer
from django.contrib.sessions.models import Session
from django.contrib.auth.models import User


class ProfileView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()

    @extend_schema(
        request=ProfileSerializer,
        responses=ProfileSerializer,
    )
    def retrieve(self, request):
        session = Session.objects.get(session_key=request.session.session_key)
        session_data = session.get_decoded()
        uid = session_data.get('_auth_user_id')
        user = Profile.objects.filter(user_id=uid)
        print(user)

        serializer = self.serializer_class(user, many=True)
        return Response(serializer.data)

    def get_feed(self, request, username):
        profile = Profile.objects.get(username=username)
        followed = profile.following.values_list('username', flat=True)
        images = PostedImage.objects.filter(author__username__in=followed)
        serializer = self.serializer_class(images, many=True)
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
    def get_feed_from_hashtag(self, request, hashtag):
        images = PostedImage.objects.filter(hashtags__icontains=hashtag)
        serializer = self.serializer_class(images, many=True)
        return Response(serializer.data)


class UserStoryView(viewsets.ModelViewSet):
    serializer_class = UserStorySerializer
    queryset = UserStory.objects.all()
    permission_classes = [IsAuthenticated]

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
