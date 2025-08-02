from django.core.validators import MinLengthValidator
from django.db import models
from django_bleach.models import BleachField


class Review(models.Model):
    content = BleachField(
        validators=[
            MinLengthValidator(10),
        ],
    )

    author = models.ForeignKey(
        to='accounts.AppUser',
        on_delete=models.CASCADE,
        related_name='reviews',
    )

    game = models.ForeignKey(
        to='games.Game',
        on_delete=models.CASCADE,
        related_name='reviews',
    )

    date_last_change = models.DateTimeField(
        auto_now=True,
    )

    class Meta:
        unique_together = ('game', 'author')
