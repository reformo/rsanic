#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from . import Users


class Main(Users):

    def invoke(self, args):

        return {'status': 200, 'data': {'name': 'Mehmet', 'surname': 'Korkmaz', 'email': 'mehmet@mkorkmaz.com'}}
