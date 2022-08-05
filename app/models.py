from operator import mod
import uuid
from django.db import models

# Create your models here.
class baseModel(models.Model):
    uid = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4())
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True

class Toda(baseModel):
    todo_title = models.CharField(max_length=100)
    todo_description = models.TextField()
    is_done = models.BooleanField(default=False)

class TimingTodo(baseModel):
    todo = models.ForeignKey(Toda,on_delete=models.CASCADE)
    timing = models.DateField()
