from django.http import Http404

import django_filters
from rest_framework.generics import (
    RetrieveAPIView, ListCreateAPIView, CreateAPIView)
from rest_framework import filters

from .models import Bet, BetSubject
from .managers import BetSubjectManager
from .serializers import BetSubjectSerializer, BetSerializer


class BetSubjectFilter(django_filters.FilterSet):
    short_description = django_filters.CharFilter(
        name='short_description', lookup_type='contains')
    long_description = django_filters.CharFilter(
        name='long_description', lookup_type='contains')
    end_datetime = django_filters.DateTimeFilter(
        name='end_datetime', lookup_type="gte")

    class Meta:
        model = BetSubject
        fields = [
            'short_description', 'long_description', 'end_datetime',
            'users', 'judge__email', 'is_private']


class BetSubjectRetreive(RetrieveAPIView):
    """ Gets information about single bet subject """
    model = BetSubject
    serializer_class = BetSubjectSerializer


class BetSubjectListCreate(ListCreateAPIView):
    """
    Returns list of bet subjects(:get) or creates new bet subject(:post)
    """
    model = BetSubject
    serializer_class = BetSubjectSerializer
    filter_class = BetSubjectFilter
    filter_backends = (filters.DjangoFilterBackend,)

    def get_queryset(self, *args, **kwargs):
        user = self.request.user
        queryset = super(BetSubjectListCreate, self).get_queryset(
            *args, **kwargs)
        if not user.is_superuser:
            queryset = queryset.filter(BetSubjectManager.user_query(user))
        return queryset

    def post(self, request):
        response = super(BetSubjectListCreate, self).post(request)
        response.data['request_data'] = request.DATA
        return response

    def pre_save(self, bet_subject):
        bet_subject.author = self.request.user


class BetCreate(CreateAPIView):
    """
    Creates new bet
    """
    model = Bet
    serializer_class = BetSerializer

    def pre_save(self, bet):
        user = self.request.user
        bet_subject_pk = int(self.kwargs['bet_subject_pk'])
        if not BetSubject.objects.get_user_queryset(
                user).filter(pk=bet_subject_pk).exists():
            raise Http404
        bet.bet_subject_id = bet_subject_pk
        bet.user = user
