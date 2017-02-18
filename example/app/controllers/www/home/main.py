#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from . import Home


class Main(Home):

    def invoke(self, args):
        r = self.redis_client
        c = r.get('c')
        if c is not None:
            r.incr('c')
            count = int(c)+1
        else:
            r.set('c', 0)
            count = 0
        return {'status': 200, 'data': {'host': self.config['redis']['host'], 'c': count}}
