from django.test import TestCase, Client
from ..models import *
import tempfile
from django.contrib.auth import get_user_model

email = 'testemail@example.com'
password = 'testpass123'


# Doc. MVP 1.1
class ProfileTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(username='testuser', email=email,
                                                        password=password)

    def test_profile_access(self):
        # Anyone should be able to get a profile by the username
        response = self.client.get('/api/profiles/username/' + self.user.username, follow=True)
        self.assertEqual(response.status_code, 200)

    def test_profile_access_own(self):
        # Owner of its own data should be able to view it in private mode
        self.assertTrue(self.client.login(email=email, password=password))
        response = self.client.get('/api/profiles/username' + self.user.username, follow=True)
        self.assertEqual(response.status_code, 200)

    def test_profile_retrieve_access(self):
        response = self.client.get('/api/profiles/', follow=True)
        self.assertEqual(response.status_code, 401)


# Doc. MVP 2.1
class ImagesTestCase(TestCase):
    def test_image_post(self):
        user = get_user_model().objects.create_user(username='testuser', email='testemail@example.com')

        PostedImage.objects.create(
            description='Test description.',
            created=datetime.now(),
            hashtags=['beach'],
            author=user,
            image=tempfile.NamedTemporaryFile(suffix=".jpg").name,
        )

        response = self.client.get('/api/postedimages/1', follow=True)
        self.assertEqual(response.status_code, 200)
