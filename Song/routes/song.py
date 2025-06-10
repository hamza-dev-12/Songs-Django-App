from django.urls import path
from ..views.song import ListSong, CreateSong, UpdateSong, DeleteSong


urlpatterns = [
    path("", ListSong.as_view()),
    path("create/", CreateSong.as_view()),
    path("update/<int:pk>/", UpdateSong.as_view()),
    path("delete/<int:pk>/", DeleteSong.as_view()),
]