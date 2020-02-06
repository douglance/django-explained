from django.urls import path
from . import views

urlpatterns = [
    path('',  views.TodoListView.as_view(), name='todo_list'),
    path('incomplete',  views.TodoIncompleteListView.as_view(),
         name='todo_incomplete_list'),
    path('create',  views.TodoCreateView.as_view(), name='todo_create'),
    path('update/<int:pk>',  views.TodoUpdateView.as_view(), name='todo_update'),
    path('delete/<int:pk>',  views.TodoDeleteView.as_view(), name='todo_delete'),
    path('complete/<int:pk>',  views.todo_complete_view, name='todo_complete'),
]
