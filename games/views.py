from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.db import IntegrityError
from django.db.models import Q
from django.db.models.aggregates import Count, Avg
from django.http import Http404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from rest_framework import status
from rest_framework.generics import CreateAPIView, get_object_or_404, UpdateAPIView
from rest_framework.response import Response

from games.forms import GameCreateForm, GameEditForm
from games.models import Game, Rating
from games.serializers import RatingSerializer
from tags.models import Tag


class GameAllView(ListView):
    model = Game
    template_name = 'games/all-games.html'
    context_object_name = 'games'
    ordering = ['name']

    def get_queryset(self):
        queryset = super().get_queryset().prefetch_related('tags')
        tag_ids = self.request.GET.getlist('tags')
        search_string = self.request.GET.get('search')
        if tag_ids:
            queryset = (queryset.filter(
                Q(tags__in=tag_ids) &
                Q(name__icontains=search_string)
            ).annotate(
                num_matched=Count(
                    'tags', filter=Q(tags__in=tag_ids))
            ).filter(
                num_matched=len(tag_ids))
            )
        return queryset.distinct()

    def get_context_data(
            self, *, object_list=..., **kwargs
    ):
        context = super().get_context_data(**kwargs)
        context['tags'] = Tag.objects.all()
        context['selected_tags'] = self.request.GET.getlist('tags')
        return context


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

        curr_user_review = (game.reviews.filter(
            author=self.request.user
        ).first()) if self.request.user.is_authenticated else None

        curr_user_rating = game.ratings.filter(
            user=self.request.user
        ).first() if self.request.user.is_authenticated else None

        if curr_user_review:
            context.update({'curr_user_review': curr_user_review})

        if curr_user_rating:
            context.update({'curr_user_rating_value': curr_user_rating.value})

        avg_rating = game.ratings.aggregate(Avg('value'))['value__avg']
        context.update({'avg_rating': avg_rating})

        return context


class GameDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Game
    success_url = reverse_lazy('all-games')
    permission_required = 'games.delete_game'
    template_name_suffix = '-confirm-delete'


class RatingCreateView(LoginRequiredMixin, CreateAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer

    def perform_create(self, serializer):
        game_id = self.kwargs.get('pk')
        game = get_object_or_404(Game, pk=game_id)

        try:
            serializer.save(
                game=game,
                user=self.request.user
            )
        except IntegrityError:
            raise

    def create(self, request, *args, **kwargs):
        try:
            return super().create(request, *args, **kwargs)
        except IntegrityError:
            return Response(
                {"detail": "You have already rated this game. Only one rating per game is allowed."},
                status=status.HTTP_400_BAD_REQUEST
            )


class RatingUpdateView(LoginRequiredMixin, UpdateAPIView):
    serializer_class = RatingSerializer

    def get_object(self):
        game_id = self.kwargs.get('pk')
        game = get_object_or_404(Game, pk=game_id)

        try:
            rating = Rating.objects.get(game=game, user=self.request.user)
            return rating
        except Rating.DoesNotExist:
            raise Http404("Rating not found for this user and game")
