from django.contrib import admin

from games.models import Game


# Register your models here.
@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    ...
