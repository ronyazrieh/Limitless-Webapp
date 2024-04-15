from django.contrib import admin
from .models import WorkoutRecord, Goal, Profile


class WorkoutRecordAdmin(admin.ModelAdmin):
    list_display = ['user', 'workout_type', 'reps', 'sets', 'created_at']
    list_filter = ['user', 'workout_type', 'created_at']

admin.site.register(WorkoutRecord, WorkoutRecordAdmin)

class GoalAdmin(admin.ModelAdmin):
    list_display = ['user', 'description', 'completed', 'created_at']
    list_filter = ['user', 'completed', 'created_at']

admin.site.register(Goal, GoalAdmin)

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'get_profile_picture']
    readonly_fields = ['get_profile_picture']

    def get_profile_picture(self, obj):
        return obj.profile_picture.url if obj.profile_picture else 'No Image'

    get_profile_picture.short_description = 'Profile Picture'

admin.site.register(Profile, ProfileAdmin)