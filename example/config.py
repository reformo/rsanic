#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
config = {
    'app_dir': os.path.dirname(os.path.abspath(__file__)) + '/app',
    'public': os.path.dirname(os.path.abspath(__file__)) + '/public',
    'host': os.environ.get('SERVICE_HOST'),
    'port': int(os.environ.get('SERVICE_PORT')),
    'base': os.environ.get('BASE_HREF'),
    'static': 'public',
    'debug': False,
    'log_access': False,
    'default_return_type': 'html',
    'not_found_method': 'www.base.not_found',
    'redis': {
        'host': os.environ.get('REDIS_HOST'),
        'port': int(os.environ.get('REDIS_PORT'))
    },
    'db': {
        'host': os.environ.get('DB_HOST'),
        'username': os.environ.get('DB_USERNAME'),
        'password': os.environ.get('DB_PASSWORD'),
        'database': os.environ.get('DB_DATABASE'),
    }
}

if os.environ.get('DEBUG') == 'On':
    config['debug'] = True
if os.environ.get('LOG_ACCESS') == 'On':
    config['log_access'] = True
