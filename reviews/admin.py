from django.contrib import admin

from reviews.models import Review


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('game', 'author', 'date_last_change')
    list_filter = ('date_last_change', 'author', 'game')
    search_fields = ('game__name', 'author__username', 'content')
    list_per_page = 100
