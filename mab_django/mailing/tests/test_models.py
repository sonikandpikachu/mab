from django.core import mail

from mock import patch

from core.tests.helpers import MabTestCase
from ..models import send_templated_email


class EmailTests(MabTestCase):

    @patch('mab_django.mailing.models.get_template')
    def test_send_templated_email(self, mocked_get_template):
        sender = self.user
        recipients = [self.admin]
        to = ['email1@mail.com', 'email2@mail.com']
        template = 'template'
        send_templated_email(template, {},
            to=to, recipients=recipients, sender=sender)
        mocked_get_template.assert_any_call('emails/template/email.txt')
        mocked_get_template.assert_any_call('emails/template/email.html')
        mocked_get_template.assert_any_call('emails/template/subject.txt')
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].to, to + [self.admin.email])
