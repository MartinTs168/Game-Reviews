from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm

from accounts.models import Profile

UserModel = get_user_model()


class AppUserCreationForm(UserCreationForm):
    class Meta:
        model = UserModel
        fields = ('username', 'email')


class ProfileBaseForm(ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'

class ProfileEditForm(ProfileBaseForm):
    class Meta(ProfileBaseForm.Meta):
        exclude = ('user', )
