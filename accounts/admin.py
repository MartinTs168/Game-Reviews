from django.contrib import admin

from accounts.models import AppUser


@admin.register(AppUser)
class AppUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_staff', 'is_active')
    search_fields = ('username', 'email')
    filter_horizontal = ('groups', 'user_permissions')
    list_per_page = 25
