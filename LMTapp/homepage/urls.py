from django.urls import path
from .views import home, workout, sample_workout

urlpatterns = [
    path('home', home, name='home'),
    path('workout/', sample_workout, name='sample_workout'),
    path('workout/<str:muscle>/', workout, name='workout'),
]
