from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    class StateChoices(models.TextChoices):
        TO_START = "to_start", "to_start"
        IN_PROGRESS = "In process", "In process"
        DONE = "Done", "Done"
    
    title = models.CharField(max_length=15)
    description = models.TextField("Description")
    user_ref = models.ForeignKey(User, on_delete=models.CASCADE)
    state = models.CharField(max_length=20, choices=StateChoices.choices, default=StateChoices.TO_START)
    
    # def __str__(self):
    #     return str(self.title)