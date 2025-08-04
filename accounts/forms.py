from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from django.forms.fields import FilePathField
from django.forms.widgets import Textarea, TextInput, PasswordInput, FileInput

from accounts.models import Profile

UserModel = get_user_model()


class AppUserCreationForm(UserCreationForm):
    class Meta:
        model = UserModel
        fields = ('username', 'email')
        widgets = {
            'email': TextInput(attrs={'class': 'form-control'}),
            'username': TextInput(attrs={'class': 'form-control'}),
            'password1': PasswordInput(attrs={
                'autocomplete': 'new-password'
            }),
            'password2': PasswordInput()
        }


class ProfileBaseForm(ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


class ProfileEditForm(ProfileBaseForm):
    class Meta(ProfileBaseForm.Meta):
        exclude = ('user',)

        widgets = {
            'bio': Textarea(attrs={
                'class': 'form-control',
                'rows': 5
            }),
            'profile_picture': FileInput(attrs={'class': 'form-control'}),
        }
