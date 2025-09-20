from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Claims customizadas
        token["username"] = user.username
        token["email"] = user.email
        token["is_staff"] = user.is_staff
        token["is_superuser"] = user.is_superuser

        # Se você tiver campos extras no CustomUser
        if hasattr(user, "telefone"):
            token["telefone"] = user.telefone

        return token

    def validate(self, attrs):
        data = super().validate(attrs)

        # Adiciona dados extras na resposta
        data.update(
            {
                "user_id": self.user.id,
                "username": self.user.username,
                "email": self.user.email,
            }
        )
        return data


# Create your views here.
