from django.urls import path

from . import views

"""
urls.py

This is where you set up your routes.

Routes assign incoming requests to Views. 

"""

urlpatterns = [
    path('',  views.function_based_view, name='function_based_view'),
    path('class',  views.ClassBasedView.as_view(), name='class_based_view'),
]
