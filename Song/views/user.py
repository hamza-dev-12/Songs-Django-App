from ..models import User
from ..serializers import UserRegisterationSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated


class ListUser(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegisterationSerializer
    permission_classes = [IsAuthenticated]


class CreateUser(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegisterationSerializer
