#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import aioredis


class Application:

    container = None
    config = None
    request = None
    redis_client = None

    def __init__(self, container=None, request=None):
        self.container = container
        self.request = request

    async def application_global(self):
        self.config = self.container.config()

    async def get_redis(self):
        if not isinstance(self.redis_client, aioredis.RedisConnection):
            self.redis_client = await aioredis.create_connection(
                (self.config['redis']['host'], self.config['redis']['port']),
                encoding='utf-8'
            )
        return self.redis_client

    async def close(self):
        self.redis_client.close()
        await self.redis_client.wait_closed()
