from django.contrib import admin
from .models import WorkoutRecord


class WorkoutRecordAdmin(admin.ModelAdmin):
    list_display = ['user', 'workout_type', 'reps', 'sets', 'created_at']
    list_filter = ['user', 'workout_type', 'created_at']

admin.site.register(WorkoutRecord, WorkoutRecordAdmin)
