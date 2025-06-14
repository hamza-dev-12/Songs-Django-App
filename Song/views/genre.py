from rest_framework import generics
from ..models import Genre
from ..serializers import GenreSerializer
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods


class ListGenres(generics.ListAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


@csrf_exempt
@require_http_methods(["PATCH"])
def update_genre(request, pk):
    try:
        type = request.GET.get("type")
        genre = Genre.objects.get(pk=pk)

        if type:
            genre.type = type

        genre.save()

        return JsonResponse({"status": 200})

    except Genre.DoesNotExist:
        return JsonResponse({"status": 400})


class CreateGenre(generics.CreateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save()


@csrf_exempt
@require_http_methods(["DELETE"])
def delete_genre_by_type(request, type):
    try:
        genre = Genre.objects.get(type=type)
        genre.delete()
        return JsonResponse({"status": 204, "message": "deleted"})

    except Genre.DoesNotExist:
        return JsonResponse({"Error": "genre doesnt exist"})
