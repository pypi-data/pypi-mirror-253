[![License: GNU GPLv3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://github.com/ashfaque/AshUtils/blob/main/LICENSE)



## How to install
```sh
pip install AshUtils
```



## Documentation
- @cache_response_redis is a django specific decorator, works with get or list method of a class based DRF view. Used to cache the API response in Redis with a default timeout of 5 mins. which can be overridden. Also you need to set `ENABLE_REDIS_RESPONSE_CACHING=1` in your project's .env file if you want to enable caching API response in redis using this decorator.
    ```python
    # Add this in settings.py file
    ENABLE_REDIS_RESPONSE_CACHING = os.getenv('ENABLE_REDIS_RESPONSE_CACHING', None)
    if ENABLE_REDIS_RESPONSE_CACHING is not None and ENABLE_REDIS_RESPONSE_CACHING != '' and bool(int(ENABLE_REDIS_RESPONSE_CACHING)):
        CACHES = {
            "default": {
                "BACKEND": "django_redis.cache.RedisCache",
                "LOCATION": "redis://127.0.0.1:6379/1",    # Adjust this based on your Redis configuration    # "redis://username:password@127.0.0.1:6379"
                "OPTIONS": {
                    "CLIENT_CLASS": "django_redis.client.DefaultClient",
                }
            }
        }
    else:
        CACHES = {
            "default": {
                "BACKEND": "django.core.cache.backends.dummy.DummyCache",
                # "LOCATION": "unique-snowflake",
            }
        }


    # Usage:-

    from AshUtils import cache_response_redis

    @cache_response_redis(timeout=15, key_prefix='API_NAME_AS_PREFIX_USED_IN_CACHE_KEY')    # ? cache_response_redis decorator should be used only for GET API's get or list method. And it should be the top most decorator.
    @sample_decorator
    def get(self, request, *args, **kwargs):
        # response = super(__class__, self).get(self, request, args, kwargs)
        # return response
        ...
    ```


- @print_db_queries is a django specific decorator, works with any method of a class based DRF view. It prints out the raw SQL queries running behind Django's ORM.
    ```python
    # Usage:-

    from AshUtils import print_db_queries

    @print_db_queries
    @sample_decorator
    def get(self, request, *args, **kwargs):
        # response = super(__class__, self).get(self, request, args, kwargs)
        # return response
        ...
    ```


- @log_db_queries  is a django specific decorator, works with any method of a class based DRF view. It logs the raw SQL queries running behind Django's ORM.
    + DJANGO_ROOT needs to be configured in settings.py, as the default log path is `DJANGO_ROOT/logs/db_query_logs.db_query_logger.log``
    + Default log file max size is 50 MB with 3 backups after rotation.
    ```python
    # Usage:-

    from AshUtils import log_db_queries

    @log_db_queries
    @sample_decorator
    def get(self, request, *args, **kwargs):
        # response = super(__class__, self).get(self, request, args, kwargs)
        # return response
        ...
    ```



## License
[GNU GPLv3](LICENSE)
