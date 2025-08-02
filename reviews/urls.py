from django.urls import path

from reviews import views

urlpatterns = [
    path('<int:game_id>/create/', views.create_review, name='create-review')
]
