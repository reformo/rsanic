#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import app.controllers.www as www


class Home(www.Application):

    def controller_global(self):
        # print('controller_global')
        return True
