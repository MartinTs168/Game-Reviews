from django import template

from accounts.models import AppUser

register = template.Library()


@register.filter(name='has_group')
def has_group(user: AppUser, group_name: str) -> bool:
    return user.is_superuser or user.groups.filter(name=group_name).exists()
