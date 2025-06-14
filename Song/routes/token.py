from django.urls import path
from ..views.token import CustomTokenObtainPairView

# from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path("", CustomTokenObtainPairView.as_view(), name="get_token"),
    # path("refresh/", TokenRefreshView.as_view(), name="refresh_token"),
]
