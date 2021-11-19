from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_page, name="register"),
    path('login/', views.login_page, name="login"),
    path('logout/', views.logout_user, name="logout"),

    path('', views.home_page, name="homepage"),

    path('games/', views.games_page, name="games"),
    path('review/<str:id>', views.reviews_page, name="review"),
    path('game/<str:id>', views.game_page, name="game"),

    path('write_review/', views.write_review, name="write_review"),
    path('update_review/<str:id>', views.update_review, name="update_review"),
    path('delete_review/<str:id>', views.delete_review, name="delete_review"),

    path('register_game/', views.register_game, name="register_game"),
    path('update_game/<str:id>', views.update_game, name="update_game"),
    path('delete_game/<str:id>', views.delete_game, name="delete_game")
]