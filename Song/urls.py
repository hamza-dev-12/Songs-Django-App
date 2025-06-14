from django.urls import path, include

urlpatterns = [
    path("token/", include("Song.routes.token")),
    path("songs/", include("Song.routes.song")),
    path("genre/", include("Song.routes.genre")),
    path("user/", include("Song.routes.user")),
    path("collection/", include("Song.routes.collection")),
]
