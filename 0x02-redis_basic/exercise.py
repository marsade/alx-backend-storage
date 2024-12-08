#!/usr/bin/env python3
'''
This script writes strings to Redis
'''
import uuid
import redis
from functools import wraps
from typing import Union, Callable, Optional


def count_calls(method: Callable) -> Callable:
    '''Counts the number of times a function is called
    Args:
        func: The function to be decorated
    Returns: The decorated function with a counter'''
    @wraps(method)
    def wrapper(self, *args, **kwargs) -> Union[str, bytes, int, float]:
        '''Wrapper function
        Args:
            *args: Positional arguments
            **kwargs: Keyword arguments
        Returns:
        The result of the function call or the transformed value if specified'''
        key = method.__qualname__
        self._redis.incr(key)
        return method(*args, **kwargs)
    return wrapper

class Cache:
    ''' A redis cache'''
    def __init__(self) -> None:
        '''Initializes the redis client'''
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        '''Set a value in Redis'''
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None) \
            -> Union[str, bytes, int, float, None]:
        '''Get a value from Redis
        Args:
            key: The key of the value to get
            fn: A function to apply to the value before returning it
        Returns: The value or None if not found'''
        val = self._redis.get(key)
        if val is None:
            return None
        return fn(val) if fn else val

    def get_str(self, key: str) -> Optional[str]:
        '''Get a string value from Redis'''
        return self.get(key, lambda x: x.decode('utf-8'))

    def get_int(self, key: str) -> Optional[int]:
        '''Get an integer value from Redis'''
        return self.get(key, int)
