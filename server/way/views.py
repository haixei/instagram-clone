from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializers import UserSerializer, CommentSerializer, PostedImageSerializer, UserStorySerializer
from .models import User, Comment, PostedImage, UserStory


class UserView(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class CommentView(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()


class PostedImageView(viewsets.ModelViewSet):
    serializer_class = PostedImageSerializer
    queryset = PostedImage.objects.all()

    @action(detail=False, methods=['get'])
    def get_feed(self, request):
        username = request.query_params['username']
        followed = User.objects.get(username=username)
        images = PostedImage.objects.filter(name__in=followed)

        return Response(images)


class StoriesView(viewsets.ModelViewSet):
    serializer_class = UserStorySerializer
    queryset = UserStory.objects.all()

    @action(detail=False, methods=['get'])
    def get_active_stories(self, request):
        username = request.query_params['username']
        # Retrieve the names of followed accounts
        followed = User.objects.get(username=username)
        stories = UserStory.objects.filter(name__in=followed)

        return Response(stories)