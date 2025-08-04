from django.db.models.aggregates import Avg, Count
from django.http import HttpRequest
from django.shortcuts import render

from games.models import Game


# Create your views here.
def home(request: HttpRequest):
    top_game = Game.objects.annotate(
        avg_rating=Avg('ratings__value'),
        ratings_count=Count('ratings')
    ).filter(ratings_count__gt=0).order_by('-avg_rating', '-ratings_count').first()
    context = {
        'top_game': top_game,
    }
    return render(request, 'common/home-page.html', context=context)
