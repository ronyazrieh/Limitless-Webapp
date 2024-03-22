# forms.py
from django import forms
from .models import WorkoutRecord

class WorkoutRecordForm(forms.ModelForm):

    class Meta:
        model = WorkoutRecord
        exclude = ['workout_type','username','user']