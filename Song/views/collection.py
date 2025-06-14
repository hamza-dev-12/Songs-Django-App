from rest_framework import generics
from ..models import Collection
from ..serializers import CollectionSerializer


class ListCollections(generics.ListAPIView):
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer


class CreateCollections(generics.CreateAPIView):
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer

    def perform_create(self, serializer):
        print(serializer)
        if serializer.is_valid():
            serializer.save()
