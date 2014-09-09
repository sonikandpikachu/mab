import os
import shutil

from django.contrib.auth import get_user_model
from django.conf import settings

from rest_framework.test import APITestCase, APIClient

from users.tests.factories import UserFactory


class MabTestCase(APITestCase):
    """ Helper Test case - general for all project"""

    def setUp(self):
        self.client = APIClient()

    @property
    def user(self):
        if not hasattr(self, '_user'):
            self._user = UserFactory(
                username='user', email='user@gmail.com', password='user')
        return self._user

    @property
    def admin(self):
        if not hasattr(self, '_admin'):
            self._admin = UserFactory(username='admin', email='admin@i.ua',
                is_superuser=True, is_staff=True, password='admin')
        return self._admin

    def login_as(self, user):
        self.assertTrue(self.client.login(
            email=user.email, password=user.username))

    def refresh_user(self, user):
        """ Gets user from database """
        user = get_user_model().objects.get(id=user.id)
        return user

    def tearDown(self):
        if os.path.exists(settings.EMAIL_FILE_PATH):
            shutil.rmtree(settings.EMAIL_FILE_PATH)
        if os.path.exists(settings.MEDIA_ROOT):
            shutil.rmtree(settings.MEDIA_ROOT)
