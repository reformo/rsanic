#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from . import Home


class Main(Home):

    def invoke(self, args):

        return {'status': 200, 'data': {'name': 'Mehmet', 'surname': 'Korkmaz', 'email': 'mehmet@mkorkmaz.com'}}
