from django.contrib.auth import get_user_model, login
from django.urls import reverse_lazy
from django.views.generic import CreateView

from accounts.forms import AppUserCreationForm

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
