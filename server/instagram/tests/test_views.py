from django.test import TestCase, Client


class ProfileTestCase(TestCase):
    def test_profile_access(self):
        # Everyone without the admin privileges should be able to view the profiles
        response = self.client.get('/api/profiles/')
        self.assertEqual(response.status_code, 200)

    def test_retrieve_wrong_uid(self):
        # Any user id that is not a string or an invalid id should return a 404 code
        response = self.client.get('/api/profiles/abc/')
        self.assertEqual(response.status_code, 404)

    def test_retrieve_session_user(self):
        # We're testing if the permissions work correctly, we only
        # want to respond with data if the user has an active session id
        response = self.client.get('/api/profiles/sessionUser', follow=True)
        self.assertEqual(response.status_code, 404)
