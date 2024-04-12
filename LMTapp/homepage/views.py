from django.shortcuts import render, redirect, get_object_or_404
from .forms import WorkoutRecordForm
from .forms import GoalForm
from .models import Goal
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    goals = Goal.objects.filter(user=request.user)
    if request.method == 'POST':
        form = GoalForm(request.POST)
        if form.is_valid():
            goal = form.save(commit=False)
            goal.user = request.user
            goal.save()
            return redirect('home')
    else:
        form = GoalForm()
    return render(request, 'homepage/home.html', {'form': form, 'goals': goals})

@login_required
def mark_goal_completed(request, goal_id):
    goal = get_object_or_404(Goal, id=goal_id)
    goal.completed = True
    goal.save()
    return redirect('home')



def success_page(request):
    return render(request, 'homepage/success.html')

def sample_workout(request):
    return render(request, 'sample_workout.html')




@login_required
def chest_workout(request, muscle):
    if request.method == 'POST':
        form = WorkoutRecordForm(request.POST)
        if form.is_valid():
            save_workout_record(request.user, muscle, form)
            return redirect('success_page')
    else:
        form = WorkoutRecordForm()
    return render(request, 'workouts/chest_workout.html', {'form': form})

@login_required
def back_workout(request, muscle):
    return handle_workout_request(request, muscle)

@login_required
def bicep_workout(request, muscle):
    return handle_workout_request(request, 'bicep')

@login_required
def tricep_workout(request, muscle):
    return handle_workout_request(request, 'tricep')

@login_required
def delts_workout(request, muscle):
    return handle_workout_request(request, 'delts')

@login_required
def quads_workout(request, muscle):
    return handle_workout_request(request, 'quads')

@login_required
def hamstring_workout(request, muscle):
    return handle_workout_request(request, 'hamstring')

@login_required
def glutes_workout(request, muscle):
    return handle_workout_request(request, 'glutes')

def save_workout_record(user, muscle, form):
    workout_record = form.save(commit=False)
    workout_record.user = user
    workout_record.username = user.username
    workout_record.workout_type = muscle
    workout_record.save()

def handle_workout_request(request, muscle):
    if request.method == 'POST':
        form = WorkoutRecordForm(request.POST)
        if form.is_valid():
            save_workout_record(request.user, muscle, form)
            return redirect('success_page')
    else:
        form = WorkoutRecordForm()
    return render(request, f'workouts/{muscle}_workout.html', {'form': form})

