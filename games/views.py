from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from games.forms import GameCreateForm
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
