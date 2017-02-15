#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import dependency_injector.containers as containers
import dependency_injector.providers as providers
import asyncio_redis
from verify import Verify

class Container(containers.DeclarativeContainer):
    """IoC container of core component providers."""

    config = providers.Configuration('config')

    routes = providers.Configuration('routes')

    redis = providers.Singleton(asyncio_redis.Connection.create).add_kwargs(host=config.redis.host, port=config.redis.port)

