from django.core.exceptions import ValidationError
from django.core.validators import validate_email as django_validate_email


def validate_email(email):
    try:
        django_validate_email(email)
        return True
    except ValidationError:
        return False
