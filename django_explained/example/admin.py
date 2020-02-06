from django.contrib import admin

from .models import Example


""" 
Django Admin
https://docs.djangoproject.com/en/3.0/ref/contrib/admin/

This is where you "register" your models for the admin.

Options:
    - fields
    - list_display
    - form widgets
    
"""


@admin.register(Example)
class ExampleAdmin(admin.ModelAdmin):
    list_display = ['text']
