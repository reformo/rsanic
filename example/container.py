#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import dependency_injector.containers as containers
import dependency_injector.providers as providers
from redis import StrictRedis


class Container(containers.DeclarativeContainer):
    """IoC container of core component providers."""

    config = providers.Configuration('config')

    routes = providers.Configuration('routes')

    redis = providers.Singleton(StrictRedis, host=config.redis.host, port=config.redis.port, db=0)

