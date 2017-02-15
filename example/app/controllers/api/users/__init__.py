#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import app.controllers.api as api


class Users(api.Application):

    def controller_global(self):
        # print('controller_global')
        return True
