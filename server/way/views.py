from django.shortcuts import render
from rest_framework import viewsets
from .serializers import UserSerializer, CommentSerializer, PostedImageSerializer
from .models import User, Comment, PostedImage


class UserView(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class CommentView(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()


class PostedImageView(viewsets.ModelViewSet):
    serializer_class = PostedImageSerializer
    queryset = PostedImage.objects.all()
