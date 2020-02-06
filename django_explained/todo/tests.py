from django.test import TestCase
from django.utils import timezone

from .models import Todo


class TodoTestCase(TestCase):
    def setUp(self):
        Todo.objects.create(task="now")
        Todo.objects.create(
            task="future", due=timezone.now() + timezone.timedelta(days=1))

    def test_todo_is_past_due(self):
        now_todo = Todo.objects.get(task="now")
        self.assertEqual(now_todo.is_past_due, True)
        future_todo = Todo.objects.get(task="future")
        self.assertEqual(future_todo.is_past_due, False)

    def test_todo_is_doneable(self):
        now_todo = Todo.objects.get(task="now")
        now_todo.toggle_done()
        self.assertEqual(now_todo.done, True)
        now_todo.toggle_done()
        self.assertEqual(now_todo.done, False)
