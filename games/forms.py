from django.forms.models import ModelForm
from django.forms.widgets import CheckboxSelectMultiple, TextInput, DateInput, Textarea, FileInput

from games.models import Game


class GameBaseForm(ModelForm):
    class Meta:
        model = Game
        fields = '__all__'

        widgets = {
            'tags': CheckboxSelectMultiple(),
            'name': TextInput(attrs={'class': 'form-control'}),
            'developer': TextInput(attrs={'class': 'form-control'}),
            'publisher': TextInput(attrs={'class': 'form-control'}),
            'available_platforms': TextInput(attrs={'class': 'form-control'}),
            'release_date': DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'description': Textarea(attrs={
                'class': 'form-control',
                'rows': 5
            }),
            'image': FileInput(attrs={'class': 'form-control'}),
        }


class GameCreateForm(GameBaseForm):
    ...


class GameEditForm(GameBaseForm):
    ...
