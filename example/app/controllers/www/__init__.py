#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Application:

    container = None
    config = None
    request = None
    redis_client = None

    def __init__(self, container=container, request=request):
        self.container = container
        self.request = request

    def application_global(self):
        self.config = self.container.config()
        self.redis_client = self.container.redis()

    def close(self):
        self.redis_client.close()