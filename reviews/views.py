from django.contrib import messages
from django.db import IntegrityError
from django.shortcuts import redirect
from django.forms import ValidationError

from reviews.forms import ReviewCreateForm


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
