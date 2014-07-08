from django.conf import settings

import factory


class UserFactory(factory.DjangoModelFactory):
    FACTORY_FOR = settings.AUTH_USER_MODEL

    email = factory.Sequence(lambda n: 'user#{}@gmail.com'.format(n))
    username = factory.Sequence(lambda n: 'user#{}'.format(n))

    @factory.post_generation
    def _set_password(self, create, extracted, *args, **kwargs):
        self.set_password(self.username)
        if create:
            self.save()
