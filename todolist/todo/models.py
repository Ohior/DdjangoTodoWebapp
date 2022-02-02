from django.db import models

# Create your models here.
# models is like a database. we will make it take one field named title
class Todo(models.Model):
    title = models.CharField(max_length=1000)

    def __str__(self):
        return self.title