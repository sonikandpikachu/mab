import os
import collections
from copy import deepcopy

from django.db import models
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context
from django.conf import settings

from django_extensions.db.models import TimeStampedModel


class Email(TimeStampedModel):
    subject = models.CharField(max_length=511)
    from_email = models.CharField(max_length=127)
    to = models.CharField(max_length=2047)
    txt_content = models.TextField()
    html_content = models.TextField()
    sender = models.ForeignKey('users.User', related_name='sended_emails',
        blank=True, null=True)
    recipients = models.ManyToManyField('users.User',
        related_name='received_emails')

    def save(self, *args, **kwargs):
        if isinstance(self.to, collections.Iterable):
            self.to = ', '.join([str(e) for e in self.to])
        return super(Email, self).save(*args, **kwargs)


def send_templated_email(template, context,
        from_email=None, to=None, sender=None, recipients=None):
    txt_template = get_template(os.path.join('emails', template, 'email.txt'))
    html_template = get_template(os.path.join('emails', template, 'email.html'))
    subject_template = get_template(os.path.join('emails', template, 'subject.txt'))
    txt_content = txt_template.render(Context(context))
    html_content = html_template.render(Context(context))
    subject = subject_template.render(Context(context))

    if from_email is None:
        from_email = settings.DEFAULT_FROM_EMAIL
    if to is None and recipients is None:
        raise ValueError('`recipients` or `to` have to be defined')
    to = [] if to is None else deepcopy(to)
    if recipients is not None:
        to += [r.email for r in recipients]

    email = Email(subject=subject, from_email=from_email, to=to,
        txt_content=txt_content, html_content=html_content)
    if sender is not None:
        email.sender = sender
    email.save()
    if recipients is not None:
        email.recipients = recipients

    msg = EmailMultiAlternatives(subject, txt_content, from_email, to)
    msg.attach_alternative(html_content, "text/html")
    msg.send()
