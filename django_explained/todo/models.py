from django.db import models
from django.utils.timezone import now


class Todo (models.Model):
    task = models.CharField(max_length=1024)
    done = models.BooleanField(default=False)
    due = models.DateTimeField(default=now, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('due', '-done')

    @property
    def is_past_due(self):
        return now() > self.due

    def toggle_done(self):
        self.done = not self.done
        self.save()

    def __str__(self):
        return self.task
