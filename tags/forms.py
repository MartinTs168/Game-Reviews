from django.forms.models import ModelForm

from tags.models import Tag


class TagBaseForm(ModelForm):
    class Meta:
        model = Tag
        exclude = ('games',)


class TagCreateForm(TagBaseForm):
    ...
