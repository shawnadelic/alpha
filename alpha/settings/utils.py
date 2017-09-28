import os

from django.core.exceptions import ImproperlyConfigured


def get_env_variable(var):
    """Get the environment variable or return exception."""
    from .base import PROJECT_NAME  # Avoid circular import
    full_var_name = "{}_{}".format(PROJECT_NAME.upper(), var)

    try:
        return os.environ[full_var_name]
    except KeyError:
        error_msg = "Set the {} variable".format(full_var_name)
        raise ImproperlyConfigured(error_msg)
