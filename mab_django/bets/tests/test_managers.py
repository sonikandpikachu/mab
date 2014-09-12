from core.tests.helpers import MabTestCase
from users.tests.factories import UserFactory
from .factories import BetSubjectFactory
from ..models import BetSubject


class BetSubjectManagerTest(MabTestCase):

    def test_get_user_queryset(self):
        user_from_users = UserFactory()
        judge = UserFactory()
        not_involved_user = UserFactory()
        BetSubjectFactory(users=[user_from_users], judge=judge)
        self.assertTrue(
            BetSubject.objects.get_user_queryset(
                user=user_from_users).exists())
        self.assertTrue(
            BetSubject.objects.get_user_queryset(user=judge).exists())
        self.assertFalse(
            BetSubject.objects.get_user_queryset(
                user=not_involved_user).exists())
