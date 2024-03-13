from django.shortcuts import render


def home(request):
    return render(request, 'homepage/home.html')

def sample_workout(request):
    return render(request, 'sample_workout.html')

def chest_workout(request):
    return render(request, 'workouts/chest_workout.html')

def back_workout(request):
    return render(request, 'workouts/back_workout.html')