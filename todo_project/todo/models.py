from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=20, default='', blank=False)
    description = models.TextField(max_length=60, default='', blank=False)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return '{} -|- {}'.format(self.title, self.user.username)

