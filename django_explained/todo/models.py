from django.db import models


class Todo (models.Model):
    task = models.CharField(max_length=1024)
    done = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.task

    def get_absolute_url(self):
        return "/todo"
