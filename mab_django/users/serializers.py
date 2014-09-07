from django.contrib.auth import get_user_model
from django.contrib import auth

from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = ('email', 'is_staff')

    def validate(self, attrs):
        if not get_user_model().objects.filter(email=attrs['email']).exists():
            raise serializers.ValidationError("no user with such email")
        return attrs

    def restore_object(self, attrs, instance=None):
        return get_user_model().objects.get(email=attrs['email'])


class CreateUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = ('email', 'password', 'auth_token')
        read_only_fields = ('auth_token',)
        write_only_fields = ('password', 'email')

    def validate(self, attrs):
        if get_user_model().objects.filter(email=attrs['email']).exists():
            raise serializers.ValidationError(
                "user with such email already exists")
        return attrs

    def restore_object(self, attrs, instance=None):
        User = get_user_model()
        user = User(email=attrs['email'])
        user.set_password(attrs['password'])
        return user


class SignInSerializer(serializers.Serializer):
    """ User authentication """

    email = serializers.EmailField(write_only=True)
    password = serializers.CharField(write_only=True)
    auth_token = serializers.CharField(read_only=True)

    def validate(self, attrs):
        self.user = auth.authenticate(
            username=attrs['email'], password=attrs['password'])
        if (not self.user) or (not self.user.is_active):
            raise serializers.ValidationError('Wrong username or password')
        return attrs

    def restore_object(self, attrs, instance=None):
        return self.user
