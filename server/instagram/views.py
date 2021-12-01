# Custom schema support
from drf_spectacular.utils import extend_schema
from rest_framework import viewsets
from .customviewsets import UpdateDestroyViewSet, DestroyCreateViewSet, NoListViewSet
from .permissions import *
from rest_framework.response import Response
from .models import Profile, Comment, PostedImage, UserStory
from .serializers import ProfileSerializer, CommentSerializer, PostedImageSerializer, UserStorySerializer, ProfilePublicSerializer
from django.contrib.sessions.models import Session
from rest_framework.decorators import action


class ProfilePublicView(UpdateDestroyViewSet):
    serializer_class = ProfilePublicSerializer
    queryset = Profile.objects.all()
    permission_classes = [IsOwnerOrReadOnly]

    @extend_schema(
        request=ProfilePublicSerializer,
        responses=ProfilePublicSerializer,
        description='This route allows you to fetch a user by their username. If you own the data, it displays'
        'in private mode.'
    )
    def get_by_username(self, request, username):
        # Try to retrieve the user, proceed if found otherwise return a 404 status
        try:
            requested_user = Profile.objects.get(username=username)
            print(requested_user)
        except Profile.DoesNotExist:
            return Response('User not found.',
                            status=404)

        # Get the user id of the user who requested the data from the session, if the session
        # doesn't exist, do not update the value
        uid = -1
        if request.session.session_key is not None:
            session = Session.objects.get(session_key=request.session.session_key)
            session_data = session.get_decoded()
            uid = session_data.get('_auth_user_id')

        # Convert the uid to an int so its comparable with requested user id
        try:
            uid = int(uid)
        except ValueError:
            return Response(status=500)

        # Return profile in a public mode if the user is not the owner of the profile
        if (uid == -1) or (uid != requested_user.user.id):
            serializer = self.get_serializer(requested_user)
            return Response(serializer.data)
        # Return in private mode
        else:
            serializer = ProfileSerializer(requested_user)
            return Response(serializer.data)


class CommentView(NoListViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()


class PostedImageView(NoListViewSet):
    serializer_class = PostedImageSerializer
    queryset = PostedImage.objects.all()
    permission_classes = [IsOwnerOrReadOnly]

    @extend_schema(
        request=PostedImageSerializer,
        responses=PostedImageSerializer,
    )
    def create(self, request, *args, **kwargs):
        # Allow access only to people who are currently logged in
        if request.session.session_key is not None:
            # If the image author matches the logged in user, create the picture
            session = Session.objects.get(session_key=request.session.session_key)
            session_data = session.get_decoded()
            uid = session_data.get('_auth_user_id')
            if uid == request.data['author']:
                serializer = self.get_serializer(data=request.data)
                serializer.is_valid(raise_exception=True)
                self.perform_create(serializer)
                headers = self.get_success_headers(serializer.data)
                return Response(serializer.data, status=201, headers=headers)
            else:
                return Response('You are not authorized to post an image for that user.', status=403)
        else:
            return Response('Log in to post an image.', status=403)

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
        description='The feed is a list of all found images that were uploaded by users who the currently logged in '
                    'user follows.'
    )
    @action(detail=False, methods=['GET'], name='feed')
    def feed(self, request):
        if request.session.session_key is not None:
            session = Session.objects.get(session_key=request.session.session_key)
            session_data = session.get_decoded()
            uid = session_data.get('_auth_user_id')

            profile = Profile.objects.get(user_id=uid)
            followed = profile.following.values_list('username', flat=True)
            images = PostedImage.objects.filter(author__username__in=followed)
            serializer = self.serializer_class(images, many=True)
            return Response(serializer.data)
        else:
            return Response('Log in to see your feed.',
                            status=403)


class UserStoryView(DestroyCreateViewSet):
    serializer_class = UserStorySerializer
    queryset = UserStory.objects.all()
    permission_classes = [IsOwnerOrReadOnly]

    @extend_schema(
        request=PostedImageSerializer,
        responses=PostedImageSerializer,
    )
    def create(self, request, *args, **kwargs):
        # Allow access only to people who are currently logged in
        if request.session.session_key is not None:
            # If the image author matches the logged in user, create the picture
            session = Session.objects.get(session_key=request.session.session_key)
            session_data = session.get_decoded()
            uid = session_data.get('_auth_user_id')
            if uid == request.data['author']:
                serializer = self.get_serializer(data=request.data)
                serializer.is_valid(raise_exception=True)
                self.perform_create(serializer)
                headers = self.get_success_headers(serializer.data)
                return Response(serializer.data, status=201, headers=headers)
            else:
                return Response('You are not authorized to post a story for that user.', status=403)
        else:
            return Response('Log in to post a story.', status=403)

    def get_by_username(self, request, username):
        try:
            stories = UserStory.objects.filter(author__username=username)
            serializer = self.serializer_class(stories, many=True)
            return Response(serializer.data)
        except UserStory.DoesNotExist:
            return Response(status=404)

    @action(detail=False, methods=['GET'], name='list_following')
    def list_following(self, request, *args, **kwargs):
        if request.session.session_key is not None:
            session = Session.objects.get(session_key=request.session.session_key)
            session_data = session.get_decoded()
            uid = session_data.get('_auth_user_id')

            profile = Profile.objects.get(user_id=uid)
            followed = profile.following.values_list('username', flat=True)
            stories = UserStory.objects.filter(author__username__in=followed)
            serializer = self.serializer_class(stories, many=True)
            return Response(serializer.data)
        else:
            return Response('Log in to see a list of stories from the people you follow.',
                            status=403)
