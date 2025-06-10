from django.urls import path, include

urlpatterns = [
    path("songs/", include("Song.routes.song")),
    path("genre/", include("Song.routes.genre")),
    path("user/", include("Song.routes.user")),
    path("collection/", include("Song.routes.collection"))
]