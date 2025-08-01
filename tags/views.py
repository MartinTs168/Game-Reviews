from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render
from django.views.generic import ListView

from tags.models import Tag


class TagAllView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Tag
    template_name = 'tags/all-tags.html'
    context_object_name = 'tags'
    permission_required = 'tags.view_tag'
