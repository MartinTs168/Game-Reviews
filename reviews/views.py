from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import IntegrityError
from django.shortcuts import redirect
from django.forms import ValidationError
from django.urls import reverse_lazy
from django.views.generic import UpdateView

from common.mixins import UserIsOwnerMixin
from reviews.forms import ReviewCreateForm, ReviewEditForm
from reviews.models import Review


# Create your views here.
def create_review(request, game_id):
    form = ReviewCreateForm(request.POST or None)

    if request.method == 'POST' and form.is_valid() and request.user.is_authenticated:
        try:
            review = form.save(commit=False)
            review.game_id = game_id
            review.author = request.user
            review.save()
            messages.success(request, "Your review has been successfully created!")
        except IntegrityError:
            messages.error(
                request,
                "You have already reviewed this game. You can only submit one review per game."
            )
        except ValidationError as ve:
            messages.error(request, ve.message)
    return redirect(request.META.get('HTTP_REFERER') + f"#{game_id}")


class ReviewEditView(LoginRequiredMixin, UserIsOwnerMixin, UpdateView):
    model = Review
    form_class = ReviewEditForm
    template_name = 'reviews/edit-review.html'

    def get_success_url(self):
        return reverse_lazy('game-details', kwargs={'pk': self.object.game.pk})

    def test_func(self):
        return self.request.user.pk == self.get_object().author.pk
