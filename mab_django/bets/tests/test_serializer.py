from django.test import TestCase

from users.tests.factories import UserFactory
from .factories import BetFactory
from ..serializers import BetSerializer


class BetSerializerTest(TestCase):

    def test_serialize(self):
        pro_users = [UserFactory() for i in range(2)]
        bet = BetFactory(pro_users=pro_users)
        serializer = BetSerializer(bet)
        data = serializer.data
        self.assertEqual(data['short_description'], bet.short_description)
        for u in pro_users:
            self.assertIn({'email': u.email}, data['pro_users'])
