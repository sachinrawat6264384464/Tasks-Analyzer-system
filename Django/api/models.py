

# Create your models here.
from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=200)
    due_date = models.DateField()
    estimated_hours = models.FloatField()
    importance = models.IntegerField()  # 1–10
    dependencies = models.JSONField(default=list)  # list of task IDs
    priority_score = models.FloatField(null=True)  # <-- add this line
    explanation = models.TextField(null=True, blank=True)
    def __str__(self):
        return self.title
