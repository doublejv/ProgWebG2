from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name="homepage"),
    path('games/', views.games_page, name="games"),
    path('review/<str:id>', views.reviews_page, name="review"),
    path('write_review/', views.write_review, name="write_review"),
    path('update_review/<str:id>', views.update_review, name="update_review"),
    path('delete_review/<str:id>', views.delete_review, name="delete_review")
]