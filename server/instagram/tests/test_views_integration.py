import json
import tempfile

import django.test.client
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from requests import Session

from instagram.models import *

username = 'testusername'
password = 'testpass123'


# Doc. MVP 1.1
class ProfileTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up two different accounts to test access to their own data and another user
        cls.user = get_user_model().objects.create_user(username=username, password=password,
                                                        email='whatever@me.com')
        cls.user_2 = get_user_model().objects.create_user(username=username + '2', password=password,
                                                          email='whatever2@me.com')
        cls.patch_data = {'username': 'changedusername'}

    def test_profile_access_public(self):
        # Anyone should be able to get a profile by the username
        response = self.client.get('/api/profiles/username/' + self.user.profile.username, follow=True)
        self.assertEqual(response.status_code, 200)

    def test_profile_access_owner(self):
        # Owner of its own data should be able to view it in private mode
        self.client.login(username=username, password=password)
        response = self.client.get('/api/profiles/username/' + self.user.profile.username, follow=True)
        self.assertEqual(response.status_code, 200)

    def test_profile_retrieve_access(self):
        response = self.client.get('/api/profiles/', follow=True)
        self.assertEqual(response.status_code, 404)

    def test_profile_patch_owner(self):
        # People who are not owners of the data cannot update the profile
        self.client.login(username=username, password=password)

        response_patch = self.client.patch('/api/profiles/' + str(self.user.id) + '/',
                                           content_type='application/json', data=json.dumps(self.patch_data))
        response_user = self.client.get('/api/profiles/username/' + self.patch_data['username'], follow=True)

        # We want to make sure that the post request is send properly and the data is saved on the other end
        self.assertEqual(response_patch.status_code, 200)
        self.assertEqual(response_user.status_code, 200)

    def test_profile_patch_unauthorized(self):
        # Check if someone can patch unauthorized
        response_patch_unauthorized = self.client.patch('/api/profiles/' + str(self.user_2.id) + '/',
                                                        content_type='application/json',
                                                        data=json.dumps(self.patch_data))
        self.assertEqual(response_patch_unauthorized.status_code, 403)

    def test_profile_delete_owner(self):
        self.client.login(username=username, password=password)
        response_delete = self.client.delete('/api/profiles/' + str(self.user.id) + '/')
        self.assertEqual(response_delete.status_code, 204)

    def test_profile_delete_unauthorized(self):
        response_delete = self.client.delete('/api/profiles/' + str(self.user.id) + '/')
        self.assertEqual(response_delete.status_code, 403)


# Doc. MVP 2.1
class ImagesTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(username=username, password=password,
                                                        email='whatever@me.com')
        PostedImage.objects.create(
            description='Test description.',
            created=datetime.now(),
            hashtags=['beach'],
            author=cls.user,
            image=tempfile.NamedTemporaryFile(suffix=".jpg").name,
        )

        cls.patch_data = {'description': 'new description'}

    def test_image_get(self):
        response = self.client.get('/api/postedimages/1', follow=True)
        self.assertEqual(response.status_code, 200)

    def test_image_create(self):
        self.client.login(username=username, password=password)
        with open('/app/media/images/2021-06-30-22-35-52-823.jpg', 'rb') as f:
            data = {
                'image': f,
                'description': 'test text',
                'created': '2021-11-29',
                'author': self.user.id
            }

            response = self.client.post('/api/postedimages/', data)
            self.assertEqual(response.status_code, 201)

    def test_image_create_unauthorized(self):
        with open('/app/media/images/2021-06-30-22-35-52-823.jpg', 'rb') as f:
            data = {
                'image': f,
                'description': 'test text',
                'created': '2021-11-29',
                'author': self.user.id
            }

            response = self.client.post('/api/postedimages/', data)
            self.assertEqual(response.status_code, 403)

    def test_image_list(self):
        response = self.client.get('/api/postedimages/', follow=True)
        self.assertEqual(response.status_code, 405)

    def test_image_delete_owner(self):
        self.client.login(username=username, password=password)
        response = self.client.delete('/api/postedimages/1/', follow=True)
        self.assertEqual(response.status_code, 204)

    def test_image_delete_unauthorized(self):
        response = self.client.delete('/api/postedimages/1/', follow=True)
        self.assertEqual(response.status_code, 403)

    def test_image_patch_owner(self):
        self.client.login(username=username, password=password)
        response = self.client.patch('/api/postedimages/1/',
                                     content_type='application/json',
                                     data=json.dumps(self.patch_data),
                                     follow=True)
        self.assertEqual(response.status_code, 200)

    def test_image_patch_unauthorized(self):
        response = self.client.patch('/api/postedimages/1/',
                                     content_type='application/json',
                                     data=json.dumps(self.patch_data),
                                     follow=True)
        self.assertEqual(response.status_code, 403)


# Doc. MVP 2.1
class UserStoryTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(username=username, password=password,
                                                        email='whatever@me.com')
        UserStory.objects.create(
            created=datetime.now(),
            author=cls.user,
            image=tempfile.NamedTemporaryFile(suffix=".jpg").name,
        )

    def test_story_list(self):
        response = self.client.get('/api/stories/', follow=True)
        self.assertEqual(response.status_code, 405)

    def test_story_get(self):
        response = self.client.get('/api/stories/1', follow=True)
        self.assertEqual(response.status_code, 405)

    def test_story_get_username(self):
        response = self.client.get('/api/stories/username/' + username, follow=True)
        self.assertEqual(response.status_code, 200)

    def test_story_create(self):
        self.client.login(username=username, password=password)
        with open('/app/media/images/2021-06-30-22-35-52-823.jpg', 'rb') as f:
            data = {
                'image': f,
                'created': '2021-11-29',
                'author': self.user.id
            }

            response = self.client.post('/api/stories/', data)
            self.assertEqual(response.status_code, 201)

    def test_story_create_unauthorized(self):
        with open('/app/media/images/2021-06-30-22-35-52-823.jpg', 'rb') as f:
            data = {
                'image': f,
                'created': '2021-11-29',
                'author': self.user.id
            }

            response = self.client.post('/api/stories/', data)
            self.assertEqual(response.status_code, 403)

    def test_story_delete(self):
        self.client.login(username=username, password=password)
        response = self.client.delete('/api/stories/1/', follow=True)
        self.assertEqual(response.status_code, 204)

    def test_story_unauthorized(self):
        response = self.client.delete('/api/stories/1/', follow=True)
        self.assertEqual(response.status_code, 403)
