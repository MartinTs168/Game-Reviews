from django.views.generic import ListView

from games.models import Game


class AllGamesView(ListView):
    model = Game
    template_name = 'games/all-games.html'
    context_object_name = 'games'
