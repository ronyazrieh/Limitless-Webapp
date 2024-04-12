# forms.py
from django import forms
from .models import WorkoutRecord
from .models import Goal

class WorkoutRecordForm(forms.ModelForm):

    class Meta:
        model = WorkoutRecord
        exclude = ['workout_type','username','user']

class GoalForm(forms.ModelForm):
    class Meta:
        model = Goal
        fields = ['description', 'target_sets', 'target_workouts']