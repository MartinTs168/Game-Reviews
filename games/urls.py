from django.urls import path

from games.views import GameAllView, GameCreateView

urlpatterns = [
    path('all/', GameAllView.as_view(), name='all-games'),
    path('create/', GameCreateView.as_view(), name='create-game'),
]
