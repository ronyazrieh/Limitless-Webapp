from django.shortcuts import render


def home(request):
    return render(request, 'homepage/home.html')

def sample_workout(request):
    return render(request, 'sample_workout.html')

def workout(request, muscle):
    context = {'muscle': muscle}
    return render(request, 'workout.html', context)