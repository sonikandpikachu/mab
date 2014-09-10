from django.test import TestCase

from users.tests.factories import UserFactory
from .factories import BetSubjectFactory
from ..serializers import BetSubjectSerializer


class BetSerializerTest(TestCase):

    def test_serialize(self):
        users = [UserFactory() for i in range(2)]
        bet = BetSubjectFactory(users=users)
        serializer = BetSubjectSerializer(bet)
        data = serializer.data
        self.assertEqual(data['short_description'], bet.short_description)
        for u, d in zip(users, data['users']):
            self.assertEqual(u.email, d['email'])
