from django.db import models
from django.conf import settings

from django_extensions.db.models import TimeStampedModel

from mailing import send_templated_email
from .managers import BetSubjectManager


class BetSubject(TimeStampedModel):
    status = models.CharField(max_length=31, default='not_executed', choices=(
        ('not_executed', 'not_executed'),
        ('executed', 'executed'))
    )
    short_description = models.CharField(max_length=127, blank=False)
    long_description = models.TextField(blank=True)
    end_datetime = models.DateTimeField()
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name='own_bets')
    judge = models.ForeignKey(
        settings.AUTH_USER_MODEL, null=True, related_name="judged_bets")
    users = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name='bets', through='Bet')
    is_private = models.BooleanField(default=True)
    # manager
    objects = BetSubjectManager()

    def __unicode__(self):
        return "{}".format(self.short_description)

    def mail_judge_about_creation(self):
        send_templated_email(
            'judge_bet_creation', {'bet_subject': self},
            recipients=[self.judge])


class Bet(TimeStampedModel):
    bet_subject = models.ForeignKey('BetSubject', related_name='bets')
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    description = models.TextField()
    is_success = models.NullBooleanField()
