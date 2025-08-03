from django.urls import path, include

from games.views import GameAllView, GameCreateView, GameEditView, GameDetailsView, GameDeleteView, RatingCreateView

urlpatterns = [
    path('all/', GameAllView.as_view(), name='all-games'),
    path('create/', GameCreateView.as_view(), name='create-game'),
    path('<int:pk>/', include([
        path('edit/', GameEditView.as_view(), name='edit-game'),
        path('details/', GameDetailsView.as_view(), name='game-details'),
        path('delete/', GameDeleteView.as_view(), name='delete-game'),
        path('ratings/create/', RatingCreateView.as_view(), name='create-rating'),
    ]))
]
