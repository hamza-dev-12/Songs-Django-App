from django.urls import path
from ..views.collection import ListCollections, CreateCollections

urlpatterns = [
    path("", ListCollections.as_view()),
    path("create/", CreateCollections.as_view()),
]
