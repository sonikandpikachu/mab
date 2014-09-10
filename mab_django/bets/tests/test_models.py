from django.core import mail

from core.tests.helpers import MabTestCase

from .factories import BetSubjectFactory


class BetSubjectTest(MabTestCase):

    def test_mail_judge(self):
        bs = BetSubjectFactory()
        bs.mail_judge_about_creation()
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].to, [bs.judge.email])
