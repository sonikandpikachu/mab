from django.test import TestCase

from users.tests.factories import UserFactory
from .factories import BetSubjectFactory, BetFactory
from ..serializers import BetSubjectSerializer, BetSerializer


class BetSubjectSerializerTest(TestCase):

    def test_serialize(self):
        users = [UserFactory() for i in range(2)]
        bet_subject = BetSubjectFactory(users=users)
        serializer = BetSubjectSerializer(bet_subject)
        data = serializer.data
        self.assertEqual(data['short_description'], bet_subject.short_description)
        for u, d in zip(users, data['users']):
            self.assertEqual(u.email, d['email'])


class BetSerializerTest(TestCase):

    def test_serialize(self):
        bet = BetFactory()
        serializer = BetSerializer(bet)
        data = serializer.data
        self.assertEqual(data['user']['email'], bet.user.email)
