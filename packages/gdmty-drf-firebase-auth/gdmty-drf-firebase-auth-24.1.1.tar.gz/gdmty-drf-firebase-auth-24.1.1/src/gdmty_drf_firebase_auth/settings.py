#!-*- coding: utf-8 -*-
"""
Authentication backend for handling firebase user.idToken from incoming
Authorization header, verifying, and locally authenticating

This package are published as free software under the terms of the Apache License, Version 2.0. Is developed by
Dirección de Gobierno Digital of the Secretaría de Innovación y Gobierno Abierto of Municipality of Monterrey.

Authors: ['César Benjamín García Martínez <mathereall@gmail.com>', ]
Email: gobiernodigital@monterrey.gob.mx
GitHub: https://github.com/gobiernodigitalmonterrey/gdmty-drf-firebase-auth
Package: gdmty_drf_firebase_auth
PyPi: https://pypi.org/project/gdmty-drf-firebase-auth/
License: Apache 2.0
"""


import os
import ast
from django.conf import settings
from rest_framework.settings import APISettings
from .utils import map_firebase_uid_to_username
import logging
from . import __title__

log = logging.getLogger(__title__)

DEFAULT_FIREBASE_AUTH_CONFIG = {
    # allow creation of new local user in db
    'FIREBASE_CREATE_LOCAL_USER': True,
    # attempt to split firebase user.display_name and set local user, first_name and last_name
    'FIREBASE_ATTEMPT_CREATE_WITH_DISPLAY_NAME': False,
    # Authorization header prefix, commonly JWT or Bearer (e.g. Bearer <token>)
    'FIREBASE_AUTH_HEADER_PREFIX': 'Bearer',
    # verify that JWT has not been revoked
    'FIREBASE_CHECK_JWT_REVOKED': True,
    # require that firebase user.email_verified is True
    'FIREBASE_AUTH_EMAIL_VERIFICATION': False,
    # function should accept firebase_admin.auth.UserRecord as argument and return str
    'FIREBASE_USERNAME_MAPPING_FUNC': map_firebase_uid_to_username
}

env_config = os.getenv('FIREBASE_AUTH_CONFIG', None)

if env_config:
    try:
        config = ast.literal_eval(env_config)
        if isinstance(dict, config):
            for key, value in config.items():
                if key in DEFAULT_FIREBASE_AUTH_CONFIG:
                    DEFAULT_FIREBASE_AUTH_CONFIG[key] = value
    except Exception as e:
        log.info(f'FIREBASE_AUTH_CONFIG - Exception: {e}')
        log.info("FIREBASE_AUTH_CONFIG no se encontró como variables de entorno, se usará la configuración de "
                 "settings.py de django si se encuentra, en caso contrario se utilizará la configuración "
                 "predeterminada.")

USER_FIREBASE_AUTH_CONFIG = getattr(settings, 'FIREBASE_AUTH_CONFIG', None)

# List of settings that may be in string import notation. Used only for compatibility.
IMPORT_STRINGS = ()

api_settings = APISettings(USER_FIREBASE_AUTH_CONFIG, DEFAULT_FIREBASE_AUTH_CONFIG, IMPORT_STRINGS)
