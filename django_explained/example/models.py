from django.db import models


class Example(models.Model):
    text = models.CharField(max_length=100)

    # Common Field Types:

    # CharField
    # TextField
    # BooleanField
    # DateTimeField
    # IntegerField
    # DecimalField
    # PositiveIntegerField
    # EmailField
    # UUIDField

    # See all field types here: https://docs.djangoproject.com/en/3.0/ref/models/fields/#field-types
