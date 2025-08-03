from django.urls import path, include

from reviews import views
from reviews.views import ReviewEditView, ReviewDeleteView

urlpatterns = [
    path('<int:game_id>/create/', views.create_review, name='create-review'),
    path('<int:pk>/', include([
        path('edit/', ReviewEditView.as_view(), name='edit-review'),
        path('delete/', ReviewDeleteView.as_view(), name='delete-review'),
    ])),
]
