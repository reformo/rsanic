#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from rsanic import Rsanic
from routes import routes
from config import config
import ujson as json


print('ApplicationConfig=', json.dumps(config, indent=4))
app = Rsanic(config=config, routes=routes, name='ExampleApp', workers=4)

if __name__ == "__main__":
    app.run()




