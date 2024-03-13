from django.urls import path
from .views import home, sample_workout, chest_workout, back_workout

urlpatterns = [
    path('', home, name='default_home'),
    path('home', home, name='home'),
    path('workout/', sample_workout, name='sample_workout'),
     path('workout/chest/', chest_workout, name='chest_workout'),
    path('workout/back/', back_workout, name='back_workout'),
]
