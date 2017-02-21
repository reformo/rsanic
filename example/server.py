#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from rsanic import Rsanic
from routes import routes
from config import config
from container import Container
import ujson as json

Container.config.update(config)
Container.routes.update(routes)
container = Container()
loop = container.loop()
print('ApplicationConfig=', json.dumps(config, indent=4))
app = Rsanic(container, name='ExampleApp')

if __name__ == "__main__":
    app.run()




