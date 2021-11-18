from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
from .filters import *

# Create your views here.


@login_required(login_url='login')
def home_page(request):
    games = Game.objects.all()
    reviews = Review.objects.all()
    users = User.objects.all()

    total_games = games.count()
    total_reviews = reviews.count()
    total_users = users.count()

    context = {'games': games, 'reviews': reviews, 'users': users, 'total_games': total_games, 'total_reviews': total_reviews, 'total_users': total_users}

    return render(request, 'accounts/dashboard.html', context)


def register_page(request):
    if request.user.is_authenticated:
        return redirect('homepage')
    else:
        form = UserForm()

        if request.method == 'POST':
            form = UserForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'User ' + form.cleaned_data.get('username') + ' registered successfully')

                return redirect('login')

        context = {'form': form}
        return render(request, 'accounts/register.html', context)


def login_page(request):
    if request.user.is_authenticated:
        return redirect('homepage')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('homepage')
            else:
                messages.info(request, 'Username/Password is incorrect')

        context = {}
        return render(request, 'accounts/login.html', context)


def logout_user(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def games_page(request):
    games = Game.objects.all()
    filter = GameFilter(request.GET, queryset=games)
    games = filter.qs

    context = {'games': games, 'filter': filter}

    return render(request, 'accounts/games.html', context)


@login_required(login_url='login')
def game_page(request, id):
    game = Game.objects.get(id=id)
    genre = game.genre
    platform = game.platform

    context = {'game': game, 'genre': genre, 'platform': platform}

    return render(request, 'accounts/game.html', context)


@login_required(login_url='login')
def reviews_page(request, id):
    review = Review.objects.get(id=id)
    game = review.game
    genre = game.genre
    platform = game.platform

    context = {'review': review, 'game': game, 'genre': genre, 'platform': platform}

    return render(request, 'accounts/review.html', context)


@login_required(login_url='login')
def write_review(request):
    form = ReviewForm()

    if request.method == 'POST':
        form = ReviewForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'accounts/review_form.html', context)


@login_required(login_url='login')
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


@login_required(login_url='login')
def delete_review(request, id):
    review = Review.objects.get(id=id)
    if request.method == 'POST':
        review.delete()
        return redirect('/')

    context = {'item': review}
    return render(request, 'accounts/delete.html', context)
