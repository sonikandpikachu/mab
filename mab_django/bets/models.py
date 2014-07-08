from django.db import models
from django.conf import settings

from django_extensions.db.models import TimeStampedModel


class Bet(TimeStampedModel):
    status = models.CharField(max_length=31, default='not_executed', choices=(
        ('not_executed', 'not_executed'),
        ('pro_won', 'pro_won'),
        ('con_won', 'con_won'),
        ('both_won', 'both_won'),
        ('both_lost', 'both_lost'))
    )
    short_description = models.CharField(max_length=127, blank=False)
    long_description = models.TextField(blank=True)
    end_datetime = models.DateTimeField()
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name='own_bets')
    pro_users = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name="pro_bets")
    con_users = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name='con_bets')
    judge = models.ForeignKey(
        settings.AUTH_USER_MODEL, null=True, related_name="judged_bets")
    is_private = models.BooleanField(default=True)

    def __unicode__(self):
        return "Bet: {}".format(self.short_description)
