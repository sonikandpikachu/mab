from django.core.management.base import BaseCommand

from ...models import User


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        admin = User.objects.create_superuser(email='admin@i.ua', password='admin')
        print admin.auth_token.key
