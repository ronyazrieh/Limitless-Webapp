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

class Goal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    target_sets = models.IntegerField(default=0)
    completed_sets = models.IntegerField(default=0)
    target_workouts = models.IntegerField(default=0)
    completed_workouts = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)  # New field to track completion
    def __str__(self):
        return self.description

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile_pictures/', default='profile_pictures/default.jpg')

    def __str__(self):
        return self.user.username + "'s Profile"