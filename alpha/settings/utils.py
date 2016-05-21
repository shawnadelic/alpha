import os

from django.core.exceptions import ImproperlyConfigured


def get_env_variable(var_name):
    """Get the environment variable or return exception."""
    from .base import PROJECT_NAME_PREFIX  # Avoid circular import
    full_variable_name = PROJECT_NAME_PREFIX + "_" + var_name

    try:
        return os.environ[full_variable_name]
    except KeyError:
        error_msg = "Set the {} variable".format(full_variable_name)
        raise ImproperlyConfigured(error_msg)
