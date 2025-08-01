from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from tags.forms import TagCreateForm
from tags.models import Tag


class TagAllView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Tag
    template_name = 'tags/all-tags.html'
    context_object_name = 'tags'
    permission_required = 'tags.view_tag'


class TagCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Tag
    form_class = TagCreateForm
    template_name = 'tags/create-tag.html'
    success_url = reverse_lazy('all-tags')
    permission_required = 'tags.add_tag'
