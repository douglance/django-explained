from django.urls import reverse_lazy
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DeleteView, CreateView, UpdateView
from .models import Todo


class TodoListView(ListView):
    model = Todo


class TodoIncompleteListView(ListView):
    model = Todo
    queryset = Todo.objects.filter(done=False)


class TodoDeleteView(DeleteView):
    model = Todo
    success_url = reverse_lazy('todo_list')


class TodoCreateView(CreateView):
    model = Todo
    fields = ['task']


class TodoUpdateView(UpdateView):
    model = Todo
    fields = ['task', 'done']


def todo_complete_view(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    todo.done = not todo.done
    todo.save()
    return redirect('todo_list')