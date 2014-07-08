import django_filters
from rest_framework.generics import RetrieveAPIView, ListCreateAPIView
from rest_framework import filters

from .models import Bet
from .serializers import BetSerializer


class BetFilter(django_filters.FilterSet):
    short_description = django_filters.CharFilter(
        name='short_description', lookup_type='contains')
    long_description = django_filters.CharFilter(
        name='long_description', lookup_type='contains')
    end_datetime = django_filters.DateTimeFilter(
        name='end_datetime', lookup_type="gte")

    class Meta:
        model = Bet
        fields = ['short_description', 'long_description', 'end_datetime',
            'con_users', 'pro_users', 'judge__email']


class BetRetreive(RetrieveAPIView):
    model = Bet
    serializer_class = BetSerializer


class BetListCreate(ListCreateAPIView):
    model = Bet
    serializer_class = BetSerializer
    filter_class = BetFilter
    filter_backends = (filters.DjangoFilterBackend,)

    def pre_save(self, bet):
        bet.author = self.request.user
