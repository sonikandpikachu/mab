from datetime import datetime, timedelta

import factory

from users.tests.factories import UserFactory
from ..models import BetSubject, Bet


class BetSubjectFactory(factory.DjangoModelFactory):
    FACTORY_FOR = BetSubject

    short_description = factory.Sequence(
        lambda n: 'bet subject short_description#{}'.format(n))
    end_datetime = datetime.now() + timedelta(days=7)
    judge = factory.SubFactory(UserFactory)
    author = factory.SubFactory(UserFactory)

    @factory.post_generation
    def users(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            for user in extracted:
                BetFactory(bet_subject=self, user=user)


class BetFactory(factory.DjangoModelFactory):
    FACTORY_FOR = Bet

    user = factory.SubFactory(UserFactory)
    bet_subject = factory.SubFactory(BetSubjectFactory)
    description = factory.Sequence(lambda n: 'bet description#{}'.format(n))
