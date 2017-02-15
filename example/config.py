#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
config = {
    'app_dir': os.path.dirname(os.path.abspath(__file__)) + '/app',
    'host': os.environ.get('SERVICE_HOST'),
    'port': os.environ.get('SERVICE_PORT'),
    'base': os.environ.get('BASE_HREF'),
    'static': 'public',
    'debug': False,
    'default_return_type': 'html',
    'not_found_method': 'www.base.not_found',
    'redis': {
        'host': os.environ.get('REDIS_HOST'),
        'port': os.environ.get('REDIS_PORT')
    }
}

if os.environ.get('DEBUG')== 'On':
    config['debug'] = True