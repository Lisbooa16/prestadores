from rest_framework_simplejwt.views import TokenObtainPairView

from custom_auth.models.custom_auth import CustomUser
from custom_auth.tokens import MyTokenObtainPairSerializer

from rest_framework.permissions import IsAuthenticated
from custom_auth.permissions import DynamicApiPermission
from rest_framework.generics import RetrieveUpdateAPIView


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class UserDetailView(RetrieveUpdateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = MyTokenObtainPairSerializer
    permission_classes = [DynamicApiPermission]
