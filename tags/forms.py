from django.forms.models import ModelForm
from django.forms.widgets import TextInput

from tags.models import Tag


class TagBaseForm(ModelForm):
    class Meta:
        model = Tag
        exclude = ('games',)

        widgets = {
            'name': TextInput(attrs={'class': 'form-control'}),
        }


class TagCreateForm(TagBaseForm):
    ...


class TagEditForm(TagBaseForm):
    ...
