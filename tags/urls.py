from django.urls import path

from tags.views import TagAllView

urlpatterns = [
    path('all/', TagAllView.as_view(), name='all-tags'),
]
