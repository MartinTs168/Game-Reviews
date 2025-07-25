# Generated by Django 5.2.4 on 2025-07-18 16:02

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, unique=True, validators=[django.core.validators.MinLengthValidator(2)])),
                ('developer', models.CharField(max_length=250, validators=[django.core.validators.MinLengthValidator(2)])),
                ('publisher', models.CharField(blank=True, max_length=250, null=True, validators=[django.core.validators.MinLengthValidator(2)])),
                ('description', models.TextField(max_length=1000, validators=[django.core.validators.MinLengthValidator(10)])),
                ('release_date', models.DateField()),
                ('available_platforms', models.CharField(max_length=200, validators=[django.core.validators.MinLengthValidator(2)])),
            ],
        ),
    ]
