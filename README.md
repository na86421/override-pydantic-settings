Overrdie Pydantic Settings
====================
<img src="https://img.shields.io/badge/python-%3E%3D%203.6-blue"/> <img src="https://img.shields.io/badge/-pydantic%20-%23E00050"/> <img src="https://img.shields.io/badge/-pytest%20-%231083CC"/>  

Settings management in Pydantic makes it easy to override settings, like below.
```py
# override settings
settgins.env = "production"
```  
However, if you want to change the setting value in each test suite in your test code,  
You need to change the values at the beginning of the test and roll back the values at the end of the test.

```py
from app.core.config import settings # Pydantic settings

def test_settings():
    # override setting value
    env = settings.ENV
    settings.ENV = "production"
    
    # assertions
    ...
    
    # rollback setting value, because in order not to affect other tests
    settings.ENV = env
```

This causes a lot of code duplication. So, in order to remove the code that occurs repeatedly, created a decorator for tests.

Features
========

You can easily override the setting value by simply applying a decorator to the test function.  
Also, when the test function is finished, the settings are automatically rolled back.

That's all.
```py
# for sync tests
@override_settings(settings=settings, ENV="production")
# for async tests
@async_override_settings(settings=settings, ENV="production")
```

Installation
============
```py
pip install override-pydantic-settings
```

How to use
-----
### For sync tests
```py
from pydantic import BaseSettings
from override_pydantic_settings import override_settings


class MySettings(BaseSettings):
    ENV: str = "dev"
    NAME: str = "Junki"
    EMAIL: str = "na66421@gmail.com"

    
settings = MySettings()


@override_settings(settings=settings, ENV="production", NAME="Junki Yoon")
def test_function():
    ...
```
### For async tests
```py
@pytest.mark.asyncio
@async_override_settings(settings=settings, ENV="production", EMAIL="na86421@naver.com")
async def test_function():
    ...
```

#### Warning
*You cannot override the setting value that does not exist.*

Development
===========
Compatible with `Python >= 3.6` 

`Python >= 3.10`, we can create async decorators using the
[asnyc context manager](https://docs.python.org/dev/library/contextlib.html#contextlib.asynccontextmanager).  
It seems that `async & sync` can be integrated into one function.  


Running tests
-------------
```bash
$ python -m venv venv
(venv)$ source venv/bin/acitave
(venv)$ pip install -r requirements.txt
(venv)$ pytest
```

License
=======
This project is licensed under the MIT license.
