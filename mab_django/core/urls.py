from django.conf.urls import patterns, url

from bets import views as bets_views
from users import views as users_views

urlpatterns = patterns(
    "",
    # bets app urls:
    url(
        regex=r"bet-subjects/(?P<pk>\d+)/$",
        view=bets_views.BetSubjectRetreive.as_view(),
        name="bet_subjects"
    ),
    url(
        regex=r"bet-subjects/$",
        view=bets_views.BetSubjectListCreate.as_view(),
        name="bet_subjects"
    ),
    url(
        regex=r"bet-subjects/(?P<bet_subject_pk>\d+)/bet/$",
        view=bets_views.BetCreate.as_view(),
        name="bet"
    ),
    # users app urls:
    url(
        regex=r"users/(?P<pk>\d+)/$",
        view=users_views.UserRetreive.as_view(),
        name="users"
    ),
    url(
        regex=r"users/$",
        view=users_views.UserCreate.as_view(),
        name="users"
    ),
    url(
        regex=r"current-user/$",
        view=users_views.UserView.as_view(),
        name="current_user"
    ),
    url(
        regex=r"signin/$",
        view=users_views.SignInView.as_view(),
        name="signin"
    ),

)
