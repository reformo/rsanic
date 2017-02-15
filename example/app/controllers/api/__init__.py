#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Application:

    container = None

    def __init__(self, container):
        self.container = container

    def application_global(self):
        return True
