import json
from datetime import datetime, timedelta

from django.core.urlresolvers import reverse

from core.tests import MabTestCase
from users.tests.factories import UserFactory
from .factories import BetSubjectFactory
from ..models import BetSubject, Bet


class BetSubjectViewsTest(MabTestCase):

    def setUp(self):
        super(BetSubjectViewsTest, self).setUp()
        self.login_as(self.user)

    def test_bet_retreive(self):
        bet = BetSubjectFactory()
        url = reverse('api:bet_subjects', args=(bet.pk, ))
        response = self.client.get(url)
        content = json.loads(response.content)
        self.assertEqual(content['short_description'], bet.short_description)
        self.assertEqual(content['judge']['email'], bet.judge.email)

    def test_bet_create(self):
        url = reverse('api:bet_subjects')
        data = {
            'short_description': 'bet short description',
            'judge': {'email': UserFactory().email},
            'end_datetime': datetime.now() + timedelta(days=7),
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 201)
        self.assertTrue(
            BetSubject.objects.get(
                short_description=data['short_description']))

    def test_bet_list(self):
        judge1 = UserFactory()
        judge2 = UserFactory()
        date1 = datetime.now() + timedelta(1)
        date2 = datetime.now() + timedelta(2)
        bets = []
        for short_description in 'desc1', 'desc2':
            for judge in judge1, judge2:
                for dt in date1, date2:
                    bets.append(BetSubjectFactory(
                        short_description=short_description, author=self.user,
                        judge=judge, end_datetime=dt))
        url = reverse('api:bet_subjects')
        # sorting by description:
        data1 = {'short_description': 'desc1'}
        data2 = {'short_description': 'desc'}
        for data in data1, data2:
            response = self.client.get(url, data)
            expected_bets = [b.id for b in BetSubject.objects.filter(
                short_description__contains=data['short_description'])]
            content = json.loads(response.content)
            self.assertEqual([b['id'] for b in content], expected_bets)
        # sorting by judge
        data = {'judge__email': judge1.email}
        response = self.client.get(url, data)
        content = json.loads(response.content)
        expected_bets = [b.id for b in BetSubject.objects.filter(judge=judge1)]
        self.assertEqual([b['id'] for b in content], expected_bets)
        # sorting by endtime and judge:
        data = {'judge__email': judge2.email, 'end_datetime': date2}
        response = self.client.get(url, data)
        content = json.loads(response.content)
        expected_bets = [b.id for b in BetSubject.objects.filter(
            judge=judge2, end_datetime=date2)]
        self.assertEqual([b['id'] for b in content], expected_bets)


class BetViewsTest(MabTestCase):

    def setUp(self):
        super(BetViewsTest, self).setUp()
        self.login_as(self.user)

    def test_scenarious(self):
        bet_subject = BetSubjectFactory(is_private=False)
        data = {'description': 'desc'}
        url = reverse('api:bets', args=(bet_subject.pk,))

        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 201)
        self.assertTrue(Bet.objects.filter(
            description=data['description'], user=self.user).exists())
