from django.contrib import admin
from django.db.models import Avg

from games.models import Game, Rating


# Register your models here.
@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ('name', 'developer', 'publisher', 'release_date', 'available_platforms', 'get_average_rating')
    list_filter = ('release_date', 'developer', 'publisher', 'tags')
    search_fields = ('name', 'developer', 'publisher',)
    ordering = ('name',)
    filter_horizontal = ('tags',)
    list_per_page = 25

    def get_average_rating(self, obj):
        avg_rating = obj.ratings.aggregate(Avg('value'))['value__avg']
        if avg_rating is not None:
            return round(avg_rating, 2)
        return 'No ratings'

    get_average_rating.short_description = 'Average Rating'


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ('game', 'user', 'value')
    list_filter = ('value', 'game')
    search_fields = ('game__name', 'user__username')
    ordering = ('game__name',)

    list_per_page = 100
