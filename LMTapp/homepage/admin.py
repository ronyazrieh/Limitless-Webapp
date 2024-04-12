from django.contrib import admin
from .models import WorkoutRecord, Goal


class WorkoutRecordAdmin(admin.ModelAdmin):
    list_display = ['user', 'workout_type', 'reps', 'sets', 'created_at']
    list_filter = ['user', 'workout_type', 'created_at']

admin.site.register(WorkoutRecord, WorkoutRecordAdmin)

class GoalAdmin(admin.ModelAdmin):
    list_display = ['user', 'description', 'completed']
    list_filter = ['user', 'completed']

admin.site.register(Goal, GoalAdmin)
