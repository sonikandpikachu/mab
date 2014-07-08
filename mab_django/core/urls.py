from django.conf.urls import patterns, url

from bets import views as bets_views

urlpatterns = patterns("",
# {% url "api:..." %}
    # companies app urls:
    url(
        regex=r"bets/(?P<pk>\d+)/$",
        view=bets_views.BetRetreive.as_view(),
        name="bets"
    ),
    url(
        regex=r"bets/$",
        view=bets_views.BetListCreate.as_view(),
        name="bets"
    ),

)
