from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializers import UserSerializer, CommentSerializer, PostedImageSerializer, UserStorySerializer
from .models import User, Comment, PostedImage, UserStory


class UserView(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    # Get user by username
    @action(detail=False, methods=['get'])
    def get_user(self, request, username):
        user = User.objects.get(username=username)
        serializer = self.serializer_class(user)
        return Response(serializer.data)


class CommentView(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()


class PostedImageView(viewsets.ModelViewSet):
    serializer_class = PostedImageSerializer
    queryset = PostedImage.objects.all()

    @action(detail=False, methods=['get'])
    def get_feed(self, request, username):
        print('test')
        user = User.objects.get(username=username)
        followed = user.following.values_list('username', flat=True)
        images = PostedImage.objects.filter(author__username__in=followed)
        serializer = self.serializer_class(images, many=True)
        return Response(serializer.data)


    @action(detail=False, methods=['get'])
    def get_feed_from_hashtag(self, request, hashtag):
        images = PostedImage.objects.filter(hashtags__icontains=hashtag)
        serializer = self.serializer_class(images, many=True)
        return Response(serializer.data)


class UserStoryView(viewsets.ModelViewSet):
    serializer_class = UserStorySerializer
    queryset = UserStory.objects.all()

    @action(detail=False, methods=['get'])
    def get_active_stories(self, request, username):
        user = User.objects.get(username=username)
        followed = user.following.values_list('username', flat=True)
        stories = UserStory.objects.filter(author__username__in=followed)
        serializer = self.serializer_class(stories, many=True)
        return Response(serializer.data)
