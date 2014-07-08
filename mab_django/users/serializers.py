from django.contrib.auth import get_user_model

from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = ('email',)

    def validate(self, attrs):
        if not get_user_model().objects.filter(email=attrs['email']).exists():
            raise serializers.ValidationError("no user with such email")
        return attrs

    def restore_object(self, attrs, instance=None):
        return get_user_model().objects.get(email=attrs['email'])
