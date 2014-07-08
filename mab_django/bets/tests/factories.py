from datetime import datetime, timedelta

import factory

from users.tests.factories import UserFactory
from ..models import Bet


class BetFactory(factory.DjangoModelFactory):
    FACTORY_FOR = Bet

    short_description = factory.Sequence(
        lambda n: 'bet short_description#{}'.format(n))
    end_datetime = datetime.now() + timedelta(days=7)
    judge = factory.SubFactory(UserFactory)

    @factory.post_generation
    def pro_users(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            for user in extracted:
                self.pro_users.add(user)

    @factory.post_generation
    def con_user(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            for user in extracted:
                self.con_user.add(user)
