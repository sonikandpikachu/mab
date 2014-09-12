from django.db import models
from django.db.models import Q


class BetSubjectManager(models.Manager):

    @classmethod
    def user_query(cls, user):
        return (Q(is_private=False) | Q(users=user) | Q(judge=user) |
                Q(author=user))

    def get_user_queryset(self, user):
        """
        Returns bet subjects which is private or user is envolved
        in this bet subject
        """
        queryset = super(BetSubjectManager, self).get_queryset()
        return queryset.filter(BetSubjectManager.user_query(user))
