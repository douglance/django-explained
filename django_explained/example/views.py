from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

"""
views.py

This is where you set up your views.

Views determine what the user sees.

They're where most of the business logic actually happens.

"""

# Function-based Views


def function_based_view(request):
    return render(request, 'function.html', {})


# Class-based Views

class ClassBasedView(View):
    text = "Hello, world from a class-based view!"

    def get(self, request):
        return render(request, 'class.html', {'text': self.text})
