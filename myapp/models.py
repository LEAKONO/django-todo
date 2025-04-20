from django.db import models
from django.contrib.auth.models import User

class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='todos')  # 🔐 Link to logged-in user
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=500)  # 🔁 lowercase for consistency
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title
