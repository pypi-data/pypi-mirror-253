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

This package is a fork of drf-firebase-auth
with some fixes and improvements.
This package also adds support for login
with email and password, and also adds support for
custom user models. And is fully integrated with gdmty-id.

"""

__title__ = 'gdmty_drf_firebase_auth'
__version__ = '24.1.1'
__description__ = (
    'Custom Django Rest Framework authentication backend for '
    'parsing Firebase uid tokens and storing as local users.'
    'This package is a fork of django-firebase-auth '
    'with some fixes and improvements. '
    'This package also adds support for login '
    'with email and password, and also adds support for '
    'custom user models. And is fully integrated with idmty.'
)
__url__ = 'https://github.com/gobiernodigitalmonterrey/gdmty-drf-firebase-auth'
__author__ = 'César Benjamín García Martínez'
__author_email__ = 'mathereall@gmail.com'
__license__ = 'Apache 2.0'
VERSION = __version__
