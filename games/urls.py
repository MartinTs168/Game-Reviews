from django.urls import path

from games.views import AllGamesView

urlpatterns = [
    path('all/', AllGamesView.as_view(), name='all-games'),
]
