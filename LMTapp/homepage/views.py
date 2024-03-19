from django.shortcuts import render


def home(request):
    return render(request, 'homepage/home.html')

def sample_workout(request):
    return render(request, 'sample_workout.html')

def chest_workout(request):
    return render(request, 'workouts/chest_workout.html')

def back_workout(request):
    return render(request, 'workouts/back_workout.html')

def bicep_workout(request):
    return render(request, 'workouts/bicep_workout.html')

def tricep_workout(request):
    return render(request, 'workouts/tricep_workout.html')

def delts_workout(request):
    return render(request, 'workouts/delts_workout.html')

def quads_workout(request):
    return render(request, 'workouts/quads_workout.html')

def hamstring_workout(request):
    return render(request, 'workouts/hamstring_workout.html')

def glutes_workout(request):
    return render(request, 'workouts/glutes_workout.html')