from django.test import TestCase

from .models import Example


class ExampleTestCase(TestCase):
    def setUp(self):
        Example.objects.create(text="test")

    def test_example(self):
        """Example text is accurate"""
        example = Example.objects.get(text="test")
        self.assertEqual(example.example_method(), 'test example')
