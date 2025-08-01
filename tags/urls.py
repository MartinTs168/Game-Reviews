from django.urls import path, include

from tags.views import TagAllView, TagCreateView, TagEditView

urlpatterns = [
    path('all/', TagAllView.as_view(), name='all-tags'),
    path('create/', TagCreateView.as_view(), name='create-tag'),
    path('<int:pk>/', include([
        path('edit/', TagEditView.as_view(), name='edit-tag'),
    ])),
]
