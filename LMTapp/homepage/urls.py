from django.urls import path
from .views import home, sample_workout, chest_workout, back_workout, bicep_workout, tricep_workout, delts_workout, quads_workout, hamstring_workout, glutes_workout

urlpatterns = [
    path('', home, name='default_home'),
    path('home', home, name='home'),
    path('workout/', sample_workout, name='sample_workout'),
     path('workout/chest/', chest_workout, name='chest_workout'),
    path('workout/back/', back_workout, name='back_workout'),
    path('workout/bicep/', bicep_workout, name='bicep_workout'),
    path('workout/tricep/', tricep_workout, name='tricep_workout'),
    path('workout/delts/', delts_workout, name='delts_workout'),
    path('workout/quads/', quads_workout, name='quads_workout'),
    path('workout/hamstring/', hamstring_workout, name='hamstring_workout'),
    path('workout/glutes/', glutes_workout, name='glutes_workout'),
]
