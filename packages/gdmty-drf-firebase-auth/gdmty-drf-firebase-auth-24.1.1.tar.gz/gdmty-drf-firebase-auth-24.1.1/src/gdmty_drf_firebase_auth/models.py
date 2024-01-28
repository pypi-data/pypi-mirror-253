#!-*- coding: utf-8 -*-

"""
Authentication backend for handling firebase user.idToken from incoming
Authorization header, verifying, and locally authenticating

This package are published as free software under the terms of the Apache License, Version 2.0. Is developed by
Dirección de Gobierno Digital of the Secretaría de Innovación y Gobierno Abierto of Municipality of Monterrey.

This package is a fork of drf-firebase-auth
    Models for storing the uid of authenticating firebase users and relating them
    to the local AUTH_USER_MODEL model.
    Author: Gary Burgmann
    Email: garyburgmann@gmail.com
    Location: Springfield QLD, Australia
    Last update: 2019-02-10

Authors: ['César Benjamín García Martínez <mathereall@gmail.com>', ]
Email: gobiernodigital@monterrey.gob.mx
GitHub: https://github.com/gobiernodigitalmonterrey/gdmty-drf-firebase-auth
Package: gdmty_drf_firebase_auth
PyPi: https://pypi.org/project/gdmty-drf-firebase-auth/
License: Apache 2.0
"""

from django.db import models
from django.conf import settings


class FirebaseUser(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=False,
        related_name='firebase_user',
        related_query_name='firebase_user',
    )
    uid = models.CharField(max_length=191, null=False,)


class FirebaseUserProvider(models.Model):
    firebase_user = models.ForeignKey(
        'FirebaseUser',
        on_delete=models.CASCADE,
        null=False,
        related_name='provider',
        related_query_name='provider',
    )
    uid = models.CharField(max_length=191, null=False,)
    provider_id = models.CharField(max_length=50, null=False,)
