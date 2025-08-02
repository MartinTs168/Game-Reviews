from django.forms import ModelForm

from reviews.models import Review


class ReviewBaseForm(ModelForm):
    class Meta:
        model = Review
        fields = ('content',)


class ReviewCreateForm(ReviewBaseForm):
    ...
