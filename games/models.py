from django.core.validators import MinLengthValidator
from django.db import models

# Create your models here.

class Game(models.Model):
    name = models.CharField(
        max_length=250,
        unique=True,
        validators=[
            MinLengthValidator(2),
        ],
    )

    developer = models.CharField(
        max_length=250,
        validators=[
            MinLengthValidator(2),
        ],
    )

    publisher = models.CharField(
        max_length=250,
        validators=[
            MinLengthValidator(2),
        ],
        null=True,
        blank=True,
    )

    description = models.TextField(
        max_length=1000,
        validators=[
            MinLengthValidator(10),
        ]
    )

    release_date = models.DateField()

    available_platforms = models.CharField(
        max_length=200,
        validators=[
            MinLengthValidator(2),
        ]
    )