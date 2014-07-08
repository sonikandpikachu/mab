from rest_framework import serializers

from users.serializers import UserSerializer
from users.models import User
from .models import Bet


class BetSerializer(serializers.ModelSerializer):

    judge = UserSerializer()
    author = UserSerializer(required=False, read_only=True)
    pro_users = UserSerializer(many=True, required=False)
    con_users = UserSerializer(many=True, required=False)

    class Meta:
        model = Bet
