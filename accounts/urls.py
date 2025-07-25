from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, include

from accounts import views
from accounts.views import ProfileDetailsView

urlpatterns = [
    path('register/', views.UserRegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

    path('profile/<uuid:pk>/', include([
        path('', ProfileDetailsView.as_view(), name='profile-details'),
        path('edit/', views.ProfileEditView.as_view(), name='profile-edit'),
    ]))
]
