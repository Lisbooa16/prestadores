from rest_framework.permissions import BasePermission, SAFE_METHODS
from rest_framework.permissions import BasePermission


class IsOwnerOrReadOnly(BasePermission):
    """
    Permite acesso somente ao dono do objeto.
    Usuários autenticados podem GET no próprio objeto,
    mas não podem alterar dados de outros.
    """

    def has_object_permission(self, request, view, obj):
        # Se for leitura (GET, HEAD, OPTIONS) → ok
        if request.method in SAFE_METHODS:
            return obj.id == request.user.id
        # Para alterações (PUT/PATCH/DELETE) → só se for o dono
        return obj.id == request.user.id


class CanOnlyPost(BasePermission):
    """
    Só permite requisições POST
    """

    def has_permission(self, request, view):
        return request.method == "POST"


class IsPrestador(BasePermission):
    message = "Somente prestadores podem acessar este recurso."

    def has_permission(self, request, view):
        return request.user.is_authenticated and getattr(
            request.user, "prestador", False
        )


class DynamicApiPermission(BasePermission):
    message = "Você não tem permissão para acessar este recurso."

    def has_permission(self, request, view):
        from custom_auth.models.permissoes import ApiPermission

        user = request.user
        if not user.is_authenticated:
            return False

        path = request.path  # ex: "/api/users/1/"
        method = request.method
        route_name = request.resolver_match.view_name

        perm = ApiPermission.objects.filter(
            user=user,
            route=route_name,
            method=method,
        ).first()

        # se existe a permissão e está liberada
        if perm and perm.can_access:
            return True

        # se existe e está negada → usar mensagem customizada
        if perm and not perm.can_access and perm.mensagem:
            self.message = perm.mensagem

        return False
