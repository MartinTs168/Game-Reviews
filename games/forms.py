from django.forms.models import ModelForm
from django.forms.widgets import CheckboxSelectMultiple

from games.models import Game


class GameBaseForm(ModelForm):
    class Meta:
        model = Game
        fields = '__all__'

        widgets = {
            'tags': CheckboxSelectMultiple()
        }


class GameCreateForm(GameBaseForm):
    class Meta(GameBaseForm.Meta):
        exclude = ('tags',)


class GameEditForm(GameBaseForm):
    ...
