from rest_framework import serializers

from users.serializers import UserSerializer
from .models import Bet, BetSubject


class BetSubjectSerializer(serializers.ModelSerializer):
    judge = UserSerializer()
    author = UserSerializer(required=False, read_only=True)
    users = UserSerializer(many=True, required=False, read_only=True)

    class Meta:
        model = BetSubject
        read_only_fields = ('status',)


class BetSerializer(serializers.ModelSerializer):
    bet_subject = BetSubjectSerializer(read_only=True)
    user = UserSerializer(read_only=True)

    class Meta:
        model = Bet
        read_only_fields = ('created', 'is_success')
