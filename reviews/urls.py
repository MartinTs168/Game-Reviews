from django.urls import path

from reviews import views
from reviews.views import ReviewEditView

urlpatterns = [
    path('<int:game_id>/create/', views.create_review, name='create-review'),
    path('<int:pk>/edit', ReviewEditView.as_view(), name='edit-review'),
]
