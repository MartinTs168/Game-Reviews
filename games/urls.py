from django.urls import path, include

from games.views import GameAllView, GameCreateView, GameEditView

urlpatterns = [
    path('all/', GameAllView.as_view(), name='all-games'),
    path('create/', GameCreateView.as_view(), name='create-game'),
    path('<int:pk>/', include([
        path('edit/', GameEditView.as_view(), name='edit-game'),
    ]))
]
