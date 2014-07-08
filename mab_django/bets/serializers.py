from rest_framework import serializers

from users.serializers import UserSerializer
from .models import Bet


class BetSerializer(serializers.ModelSerializer):

    judge = UserSerializer()
    author = UserSerializer()
    pro_users = UserSerializer(many=True)
    con_users = UserSerializer(many=True)

    class Meta:
        model = Bet
