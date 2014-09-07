import json

from django.core.urlresolvers import reverse

from core.tests import MabTestCase
from .factories import UserFactory
from ..models import User


class UserViewTest(MabTestCase):

    def test_user_retreive(self):
        self.login_as(self.user)
        user = UserFactory()
        url = reverse('api:users', args=(user.id,))
        response = self.client.get(url)
        content = json.loads(response.content)
        self.assertEqual(content['email'], user.email)

    def test_user_create(self):
        url = reverse('api:users')
        data = {'email': 'test_user@gmail.com', 'password': 'test_password'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 201)
        content = json.loads(response.content)
        user = User.objects.get(email=data['email'])
        self.assertEqual(content['auth_token'], user.auth_token.key)

    def test_signin(self):
        url = reverse('api:signin')
        # signing in new user
        response = self.client.get(url)
        self.assertEqual(response.status_code, 405)
        data = {
            'email': self.user.email,
            'password': self.user.username,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(User.objects.get(email=data['email']))

    def test_current_user(self):
        url = reverse("api:current_user")
        self.login_as(self.user)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        content = json.loads(response.content)
        self.assertEqual(content['email'], self.user.email)
