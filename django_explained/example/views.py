from django.shortcuts import render
from django.http import HttpResponse
from django.views import View


def function_based_view(request):
    return render(request, 'function.html', {})


class ClassBasedView(View):
    text = "Hello, world from a class-based view!"

    def get(self, request):
        return render(request, 'class.html', {'text': self.text})
