import re
from django.core.exceptions import ValidationError


def validate_password_length(password):
    if len(password) < 8:
        return False

    # Ein Regulärer Ausdruck, der überprüft, ob das Passwort mindestens ein Sonderzeichen enthält.
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        raise ValidationError(
            'The password must be at least 8 characters long')

    return True
