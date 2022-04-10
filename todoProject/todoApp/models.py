from django.db import models

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    deadline = models.DateTimeField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.title