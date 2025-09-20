from django.urls import path

from custom_auth.views import CustomTokenObtainPairView, UserDetailView
from rest_framework_simplejwt.views import TokenRefreshView


urlpatterns = [
    path("token/", CustomTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("user/<int:pk>/", UserDetailView.as_view(), name="user_detail"),
]
