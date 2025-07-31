from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView

from games.forms import GameCreateForm, GameEditForm
from games.models import Game


class GameAllView(ListView):
    model = Game
    template_name = 'games/all-games.html'
    context_object_name = 'games'


class GameCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Game
    form_class = GameCreateForm
    template_name = 'games/create-game.html'
    success_url = reverse_lazy('all-games')
    permission_required = 'games.add_game'


class GameEditView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Game
    form_class = GameEditForm
    template_name = 'games/edit-game.html'
    success_url = reverse_lazy('all-games')
    permission_required = 'games.change_game'
