#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from . import Home


class Main(Home):

    async def invoke(self, args):

        r = await self.get_redis()
        c = await r.get('c')
        if c is not None:
            await r.incr('c')
            count = int(c)+1
        else:
            await r.set('c', 0)
            count = 0
        return {'status': 200, 'data': {'host': self.config['redis']['host'], 'c': count}}

