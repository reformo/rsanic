#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import aioredis


class Application:

    config = None
    request = None
    redis_client = None

    def __init__(self, config=None, request=None):
        self.config = config
        self.request = request

    async def application_global(self):
        pass

    async def get_redis(self):
        if self.redis_client is None:
            self.redis_client = await aioredis.create_redis(
                (self.config['redis']['host'], self.config['redis']['port']),
                encoding='utf-8'
            )
        return self.redis_client

    async def close(self):
        self.redis_client.close()
        await self.redis_client.wait_closed()
