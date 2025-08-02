from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView

from games.forms import GameCreateForm, GameEditForm
from games.models import Game
from tags.models import Tag


class GameAllView(ListView):
    model = Game
    template_name = 'games/all-games.html'
    context_object_name = 'games'
    ordering = ['name']


class GameCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Game
    form_class = GameCreateForm
    template_name = 'games/create-game.html'
    permission_required = 'games.add_game'

    def get_success_url(self):
        return reverse_lazy('game-details', kwargs={'pk': self.object.pk})


class GameEditView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Game
    form_class = GameEditForm
    template_name = 'games/edit-game.html'
    permission_required = 'games.change_game'

    def get_success_url(self):
        return reverse_lazy('game-details', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['available_tags'] = Tag.objects.all()
        context['selected_tags'] = self.object.tags.all()
        return context

    def form_valid(self, form):
        response = super().form_valid(form)
        selected_tag_ids = self.request.POST.getlist('tags')
        self.object.tags.clear()
        if selected_tag_ids:
            self.object.tags.add(*selected_tag_ids)
        return response


class GameDetailsView(DetailView):
    model = Game
    template_name = 'games/details-game.html'

    def get_queryset(self):
        return self.model.objects.prefetch_related('tags', 'reviews', 'reviews__author')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        game = context['object']

        curr_user_review = game.reviews.filter(
            author=self.request.user).first() if self.request.user.is_authenticated else None

        if curr_user_review:
            context.update({'curr_user_review': curr_user_review})

        return context


class GameDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Game
    success_url = reverse_lazy('all-games')
    permission_required = 'games.delete_game'
    template_name_suffix = '-confirm-delete'
