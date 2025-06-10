from django.urls import path
from ..views.genre import ListGenres, CreateGenre, update_genre, delete_genre_by_type

urlpatterns = [
    path("", ListGenres.as_view()),
    path("create/", CreateGenre.as_view()),
    path("update/<int:pk>/", update_genre),
    path("delete/<str:type>/", delete_genre_by_type),
]