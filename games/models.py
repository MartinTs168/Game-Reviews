from cloudinary.models import CloudinaryField
from django.core.validators import MinLengthValidator, MaxValueValidator, MinValueValidator
from django.db import models

from common.validators import FileSizeValidator


class Game(models.Model):
    MAX_IMAGE_SIZE_MB = 5

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

    image = CloudinaryField(
        'image',
        validators=[
            FileSizeValidator(MAX_IMAGE_SIZE_MB)
        ],
    )

    tags = models.ManyToManyField(
        to='tags.Tag',
        related_name='games',
        blank=True,
    )

    def __str__(self):
        return self.name


class Rating(models.Model):
    value = models.PositiveSmallIntegerField(
        validators=[
            MaxValueValidator(5),
            MinValueValidator(1),
        ]
    )

    game = models.ForeignKey(
        to=Game,
        on_delete=models.CASCADE,
        related_name='ratings',
    )

    user = models.ForeignKey(
        to='accounts.AppUser',
        on_delete=models.CASCADE,
        related_name='ratings',
    )

    class Meta:
        unique_together = ('game', 'user')
