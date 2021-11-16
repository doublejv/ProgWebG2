from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home_page(request):
    return render(request, 'accounts/dashboard.html')


def games_page(request):
    return render(request, 'accounts/games.html')


def users_page(request):
    return render(request, 'accounts/users.html')
