from django.test import TestCase

from .models import Example


"""
tests.py

This is where you put your tests.

Tests can be run with:

`python manage.py test`

or 

`python manage.py test $APP_NAME`
"""


class ExampleTestCase(TestCase):
    def setUp(self):
        Example.objects.create(text="test")

    def test_example(self):
        """Example text is accurate"""
        example = Example.objects.get(text="test")
        self.assertEqual(example.example_method(), 'test example')
