from django.contrib import admin

from .models import Example

# This is where you "register" your models for the admin.

# You can configure your admin items

# list_display
# form widgets
#


@admin.register(Example)
class ExampleAdmin(admin.ModelAdmin):
    list_display = ['text']
