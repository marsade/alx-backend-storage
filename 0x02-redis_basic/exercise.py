#!/usr/bin/env python3
'''
This script writes strings to Redis
'''

import uuid
import redis
from typing import Union

class Cache:
    ''' A redis cache'''
    def __init__(self) -> None:
        '''Initializes the redis client'''
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, int, float, bool]) -> str:
        '''Set a value in Redis'''
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
