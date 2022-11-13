import pytest
from pydantic import BaseSettings

from override_settings import async_override_settings, override_settings, check_value


class MySettings(BaseSettings):
    ENV: str = "dev"
    NAME: str = "Junki"
    EMAIL: str = "na66421@gmail.com"


settings = MySettings()


@pytest.mark.asyncio
@async_override_settings(settings=settings, ENV="production", NAME="Junki Yoon")
async def test_async_override_settings():
    async def print_async():
        print("This is async function.")

    await print_async()

    assert settings.ENV == "production"
    assert settings.NAME == "Junki Yoon"


@override_settings(settings=settings, ENV="stage", EMAIL="na86421@naver.com")
def test_override_settings():
    assert settings.ENV == "stage"
    assert settings.EMAIL == "na86421@naver.com"


def test_rolled_back_settings():
    assert settings.ENV == "dev"
    assert settings.NAME == "Junki"
    assert settings.EMAIL == "na66421@gmail.com"


def test_check_value():
    with pytest.raises(ValueError):
        check_value(settings=dict(), overrides=dict())
    with pytest.raises(ValueError):
        check_value(settings=settings, overrides="fake dict")
