from django.urls import path
from .views import home, chest_workout, back_workout, bicep_workout, tricep_workout, delts_workout, quads_workout, hamstring_workout, glutes_workout, success_page, mark_goal_completed, workout_page, profile_page
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', home, name='default_home'),
    path('home/', home, name='home'),
    path('workout/chest/<str:muscle>/', chest_workout, name='chest_workout'),
    path('workout/back/<str:muscle>/', back_workout, name='back_workout'),
    path('workout/bicep/<str:muscle>/', bicep_workout, name='bicep_workout'),
    path('workout/tricep/<str:muscle>/', tricep_workout, name='tricep_workout'),
    path('workout/delts/<str:muscle>/', delts_workout, name='delts_workout'),
    path('workout/quads/<str:muscle>/', quads_workout, name='quads_workout'),
    path('workout/hamstring/<str:muscle>/', hamstring_workout, name='hamstring_workout'),
    path('workout/glutes/<str:muscle>/', glutes_workout, name='glutes_workout'),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('workout/', workout_page, name='workout_page'),
    path('profile/', profile_page, name='profile_page'),
    path('success/', success_page, name='success_page'),
    path('mark-goal-completed/<int:goal_id>/', mark_goal_completed, name='mark_goal_completed'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)