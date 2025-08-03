from django.forms import ModelForm, ValidationError
from django.utils.html import strip_tags

from reviews.models import Review


class ReviewBaseForm(ModelForm):
    class Meta:
        model = Review
        fields = ('content',)

    def clean_content(self):
        content = self.cleaned_data['content']

        text_only = strip_tags(content)
        if not text_only.strip():
            raise ValidationError('Review content cannot be empty.')

        return content


class ReviewCreateForm(ReviewBaseForm):
    ...


class ReviewEditForm(ReviewBaseForm):
    ...
