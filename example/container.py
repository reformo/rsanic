#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import dependency_injector.containers as containers
import dependency_injector.providers as providers
import asyncio


class Container(containers.DeclarativeContainer):
    """IoC container of core component providers."""

    config = providers.Configuration('config')

    routes = providers.Configuration('routes')

    loop = providers.Singleton(asyncio.get_event_loop)

