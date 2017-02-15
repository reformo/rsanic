#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from rsanic import Rsanic
from routes import routes
from config import config
from container import Container

Container.config.update(config)
Container.routes.update(routes)
container = Container()

app = Rsanic(container, name='ExampleApp')

if __name__ == "__main__":
    app.run()
