from django.urls import path

from tags.views import TagAllView, TagCreateView

urlpatterns = [
    path('all/', TagAllView.as_view(), name='all-tags'),
    path('create/', TagCreateView.as_view(), name='create-tag'),
]
