from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse, reverse_lazy
from django.utils.timezone import now
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from .models import Todo


class TodoListView(ListView):
    model = Todo
    context_object_name = 'todos'

    def get_queryset(self, **kwargs):
        queryset = super().get_queryset()
        filter = self.kwargs.get('filter')

        if filter == "complete":
            queryset = queryset.filter(done=True)
        if filter == "incomplete":
            queryset = queryset.filter(done=False)
        if filter == "overdue":
            queryset = queryset.filter(due__lte=now())

        return queryset


class TodoIncompleteListView(ListView):
    model = Todo
    context_object_name = 'todos'
    queryset = Todo.objects.filter(done=False)


class TodoDeleteView(DeleteView):
    model = Todo
    success_url = reverse_lazy('todo_list')


class TodoCreateView(CreateView):
    model = Todo
    fields = ['task', 'due']
    success_url = reverse_lazy('todo_list')


class TodoUpdateView(UpdateView):
    model = Todo
    fields = ['task', 'due', 'done']
    success_url = reverse_lazy('todo_list')


def todo_complete_view(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    todo.toggle_done()
    return redirect('todo_list')
