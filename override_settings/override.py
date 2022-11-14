import contextlib
from functools import wraps
from pydantic import BaseSettings


def async_override_settings(settings, **overrides):
    """
    Override settings for Async function.
    After the called function is finished, the settings are roll back.
    """

    def decorator(func):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            check_value(settings, overrides)

            original = {}
            try:
                for key, value in overrides.items():
                    original[key] = getattr(settings, key)
                    setattr(settings, key, value)

                await func(*args, **kwargs)

            finally:
                for key, value in original.items():
                    setattr(settings, key, value)

        return wrapper

    return decorator


@contextlib.contextmanager
def override_settings(settings, **overrides):
    """
    Override settings for Sync function.
    After the called function is finished, the settings are roll back.
    """

    check_value(settings, overrides)

    original = {}
    try:
        for key, value in overrides.items():
            original[key] = getattr(settings, key)
            setattr(settings, key, value)

        yield

    finally:
        for key, value in original.items():
            setattr(settings, key, value)


def check_value(settings, overrides):
    if not isinstance(settings, BaseSettings):
        raise ValueError("settings must be of type pydantic.BaseSettings.")

    if not isinstance(overrides, dict):
        raise ValueError("overrides must be of type dict.")
