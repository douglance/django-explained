from django.apps import AppConfig


""" 
apps.py

https://docs.djangoproject.com/en/3.0/ref/applications/#configuring-applications

This file is used to configure this Django "app" itself.

Rarely used. 

I've only used it to set up a verbose name.

"""


class ExampleConfig(AppConfig):
    name = 'example'
