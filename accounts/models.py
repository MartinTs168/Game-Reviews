import uuid

from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models

from accounts.managers import AppUserManager
from common.validators import FileSizeValidator


class AppUser(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(
        primary_key=True,
        editable=False,
        default=uuid.uuid4,
    )

    email = models.EmailField(
        unique=True,
    )

    username = models.CharField(
        unique=True,
        max_length=100,
    )

    is_active = models.BooleanField(
        default=True,
    )

    is_staff = models.BooleanField(
        default=False,
    )

    objects = AppUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']


class Profile(models.Model):
    MAX_PICTURE_SIZE_MB = 5

    user = models.OneToOneField(
        to=AppUser,
        on_delete=models.CASCADE,
        related_name='profile',
        primary_key=True,
    )

    profile_picture = models.ImageField(
        upload_to='profile_pictures/',
        null=True,
        blank=True,
        validators=[
            FileSizeValidator(MAX_PICTURE_SIZE_MB)
        ],
    )

    bio = models.CharField(
        max_length=300,
        null=True,
        blank=True,
        help_text='Brief bio about yourself',
    )
