import django_filters
from rest_framework.generics import RetrieveAPIView, ListCreateAPIView
from rest_framework import filters

from .models import Bet, BetSubject
from .serializers import BetSubjectSerializer


class BetSubjectFilter(django_filters.FilterSet):
    short_description = django_filters.CharFilter(
        name='short_description', lookup_type='contains')
    long_description = django_filters.CharFilter(
        name='long_description', lookup_type='contains')
    end_datetime = django_filters.DateTimeFilter(
        name='end_datetime', lookup_type="gte")

    class Meta:
        model = BetSubject
        fields = ['short_description', 'long_description', 'end_datetime',
            'users', 'judge__email']


class BetRetreive(RetrieveAPIView):
    """ Gets information about single bet """
    model = BetSubject
    serializer_class = BetSubjectSerializer


class BetListCreate(ListCreateAPIView):
    """ Returns list of bets(:get) or creates new bet(:post) """
    model = BetSubject
    serializer_class = BetSubjectSerializer
    filter_class = BetSubjectFilter
    filter_backends = (filters.DjangoFilterBackend,)

    def pre_save(self, bet):
        bet.author = self.request.user
