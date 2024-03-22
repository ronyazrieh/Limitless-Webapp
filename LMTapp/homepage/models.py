from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class WorkoutRecord(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=150)
    workout_type = models.CharField(max_length=20)
    reps = models.IntegerField()
    sets = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)