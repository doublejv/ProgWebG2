from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page),
    path('games/', views.games_page),
    path('users/', views.users_page),
]