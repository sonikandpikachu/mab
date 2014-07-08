import os
import shutil

from django.contrib.auth import get_user_model
from django.conf import settings

from rest_framework.test import APITestCase

from users.tests.factories import UserFactory


class MabTestCase(APITestCase):
    """ Helper Test case - general for all project"""

    def setUp(self):
        self.user = UserFactory(
            username='user', email='user@gmail.com', password='user')

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
