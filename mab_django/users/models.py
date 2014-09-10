from django.contrib.auth.models import AbstractUser, BaseUserManager

from rest_framework.authtoken.models import Token


AbstractUser._meta.get_field('email')._unique = True
AbstractUser._meta.get_field('email').blank = False
AbstractUser._meta.get_field('username').blank = True
AbstractUser._meta.get_field('username')._unique = False


class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **kwargs):
        user = self.model(email=email, **kwargs)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **kwargs):
        user = self.model(
            email=email, is_staff=True, is_superuser=True, **kwargs)
        user.set_password(password)
        user.save()
        return user


class User(AbstractUser):
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = UserManager()

    def __unicode__(self):
        return self.email

    def save(self, *args, **kwargs):
        created = self.pk is None
        saved = super(User, self).save(*args, **kwargs)
        if created:
            Token.objects.create(user=self)
        return saved
