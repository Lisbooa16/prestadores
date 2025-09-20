from django.db import models
from django.conf import settings
from django.urls import get_resolver

from django.urls import get_resolver, URLPattern, URLResolver


def list_urls(patterns=None, prefix=""):
    """
    Percorre todas as rotas registradas no projeto (incluindo includes)
    e retorna uma lista de tuplas (path, name).
    """
    if patterns is None:
        patterns = get_resolver().url_patterns

    urls = []
    for pattern in patterns:
        if isinstance(pattern, URLPattern):  # rota simples
            route = prefix + str(pattern.pattern)
            name = pattern.name or route  # se não tiver name, usa o path
            urls.append((route, name))
        elif isinstance(pattern, URLResolver):  # include(...)
            urls += list_urls(pattern.url_patterns, prefix + str(pattern.pattern))
    return urls


def get_all_routes():
    """
    Retorna lista para usar como choices no admin:
    - label = "name (path)"
    - value = name
    """
    routes = []
    for route, name in list_urls():
        routes.append((name, f"{name}  ({route})"))
    return routes


class ApiPermission(models.Model):
    METHOD_CHOICES = [
        ("GET", "GET"),
        ("POST", "POST"),
        ("PUT", "PUT"),
        ("PATCH", "PATCH"),
        ("DELETE", "DELETE"),
    ]

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="api_permissions",
    )
    route = models.CharField("Rota", max_length=255)
    method = models.CharField(max_length=10, choices=METHOD_CHOICES)
    can_access = models.BooleanField(default=False)
    mensagem = models.CharField(
        "Mensagem de negação", max_length=255, blank=True, null=True
    )

    class Meta:
        unique_together = ("user", "route", "method")

    def __str__(self):
        return f"{self.user.email} - {self.method} {self.route} ({'✔' if self.can_access else '❌'})"
