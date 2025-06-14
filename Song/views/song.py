from ..models import Song
from ..serializers import SongSerializer
from rest_framework import generics


class ListSong(generics.ListAPIView):
    serializer_class = SongSerializer

    def get_queryset(self):
        queryset = Song.objects.all()

        search_by = self.request.query_params.get("search_by")
        search_value = self.request.query_params.get("search_value")
        sort_by = self.request.query_params.get("sort_by")
        year = self.request.query_params.get("year")

        if search_by and search_value:
            kwargs = {f"{search_by}": search_value}
            queryset = queryset.filter(**kwargs)

        if year:
            queryset = queryset.filter(**{"published_date__year": year})

        if sort_by:
            queryset.order_by(sort_by)

        return queryset


class CreateSong(generics.CreateAPIView):
    serializer_class = SongSerializer

    def perform_create(self, serializer):
        if serializer.is_valid():
            # print(self.request)
            serializer.save()


class UpdateSong(generics.UpdateAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    lookup_field = "pk"

    def perform_update(self, serializer):
        if serializer.is_valid():
            serializer.save()


class DeleteSong(generics.DestroyAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    lookup_field = "pk"
