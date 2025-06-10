from django.urls import path
from ..views.user import ListUser, CreateUser

urlpatterns = [
    path("", ListUser.as_view()),
    path("create/", CreateUser.as_view())
]