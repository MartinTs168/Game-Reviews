from django.contrib.auth import get_user_model, login
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView

from accounts.forms import AppUserCreationForm, ProfileEditForm
from accounts.models import Profile
from common.mixins import UserIsOwnerMixin

# Create your views here.
UserModel = get_user_model()


class UserRegisterView(CreateView):
    model = UserModel
    form_class = AppUserCreationForm
    success_url = reverse_lazy('home')
    template_name = 'accounts/register.html'

    def form_valid(self, form):
        response = super().form_valid(form)
        # Note: signal for profile creation

        if response.status_code in (301, 302,):
            login(self.request, self.object)

        return response


class ProfileDetailsView(LoginRequiredMixin, UserIsOwnerMixin, DetailView):
    model = Profile
    context_object_name = 'profile'
    template_name = 'accounts/profile-details.html'
    queryset = Profile.objects.prefetch_related('user')


class ProfileEditView(LoginRequiredMixin, UserIsOwnerMixin, UpdateView):
    model = Profile
    form_class = ProfileEditForm
    template_name = 'accounts/profile-edit.html'

    def get_success_url(self):
        return reverse_lazy('profile-details', kwargs={'pk': self.object.pk})
