import json

from django.core.urlresolvers import reverse

from core.tests import MabTestCase
from .factories import UserFactory
from ..models import User


class UserViewTest(MabTestCase):

    def test_user_retreve(self):
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
        self.assertTrue(User.objects.get(email=data['email']))

    def test_signin(self):
        url = reverse('api:signin')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 405)
        data = {
            'email': self.user.email,
            'password': self.user.username,
        }
        response = self.client.post(url, data=data)
        print response.content
        self.assertEqual(response.status_code, 200)
        self.assertTrue(User.objects.get(email=data['email']))
