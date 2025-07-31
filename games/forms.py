from django.forms.models import ModelForm

from games.models import Game


class GameBaseForm(ModelForm):
    class Meta:
        model = Game
        fields = '__all__'


class GameCreateForm(GameBaseForm):
    ...


class GameEditForm(GameBaseForm):
    ...
