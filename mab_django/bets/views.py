import django_filters
from rest_framework.generics import RetrieveAPIView, ListCreateAPIView

from .models import Bet
from .serializers import BetSerializer


class BetFilter(django_filters.FilterSet):
    short_description = django_filters.StringFilter(
        name='short_description', lookup_type='in')
    long_description = django_filters.StringFilter(
        name='long_description', lookup_type='in')

    class Meta:
        model = Bet
        fields = ['short_description', 'long_description', 'end_datetime',
            'con_users', 'pro_users', 'judge']


class BetRetreive(RetrieveAPIView):
    model = Bet
    serializer_class = BetSerializer


class BetListCreate(ListCreateAPIView):
    model = Bet
    serializer_class = BetSerializer
    filter_class = BetFilter
