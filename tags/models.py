from django.db import models

# Create your models here.
class Tag(models.Model):
    name = models.CharField(
        max_length=50,
        unique=True,
    )

    games = models.ManyToManyField(
        to='games.Game',
        related_name='tags',
        blank=True,
    )