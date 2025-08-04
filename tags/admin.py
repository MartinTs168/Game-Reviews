from django.contrib import admin

from tags.models import Tag


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'get_games_count')
    search_fields = ('name',)
    ordering = ('name',)

    def get_games_count(self, obj):
        return obj.games.count()

    get_games_count.short_description = 'Games Count'
