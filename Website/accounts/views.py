from django.shortcuts import render, redirect
from .models import *
from .forms import *
from .filters import *

# Create your views here.


def home_page(request):
    games = Game.objects.all()
    reviews = Review.objects.all()
    users = User.objects.all()

    total_games = games.count()
    total_reviews = reviews.count()
    total_users = users.count()

    context = {'games': games, 'reviews': reviews, 'users': users, 'total_games': total_games, 'total_reviews': total_reviews, 'total_users': total_users}

    return render(request, 'accounts/dashboard.html', context)


def games_page(request):
    games = Game.objects.all()
    filter = GameFilter(request.GET, queryset=games)
    games = filter.qs

    context = {'games': games, 'filter': filter}

    return render(request, 'accounts/games.html', context)


def game_page(request, id):
    game = Game.objects.get(id=id)
    genre = game.genre
    platform = game.platform

    context = {'game': game, 'genre': genre, 'platform': platform}

    return render(request, 'accounts/game.html', context)


def reviews_page(request, id):
    review = Review.objects.get(id=id)
    game = review.game
    genre = game.genre
    platform = game.platform

    context = {'review': review, 'game': game, 'genre': genre, 'platform': platform}

    return render(request, 'accounts/review.html', context)


def write_review(request):
    form = ReviewForm()

    if request.method == 'POST':
        form = ReviewForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'accounts/review_form.html', context)


def update_review(request, id):
    review = Review.objects.get(id=id)
    form = ReviewForm(instance=review)

    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)

        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'accounts/review_form.html', context)


def delete_review(request, id):
    review = Review.objects.get(id=id)
    if request.method == 'POST':
        review.delete()
        return redirect('/')

    context = {'item': review}
    return render(request, 'accounts/delete.html', context)
