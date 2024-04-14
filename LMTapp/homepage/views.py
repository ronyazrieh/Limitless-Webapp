from django.shortcuts import render, redirect, get_object_or_404
from .forms import WorkoutRecordForm
from .models import WorkoutRecord
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
    recent_workout = WorkoutRecord.objects.filter(user=request.user, workout_type=muscle).order_by('-created_at').first()
    incomplete_goals = Goal.objects.filter(user=request.user, completed=False).order_by('-created_at')[:3]
    return handle_workout_request(request, muscle, recent_workout, incomplete_goals)

@login_required
def back_workout(request, muscle):
    recent_workout = WorkoutRecord.objects.filter(user=request.user, workout_type=muscle).order_by('-created_at').first()
    incomplete_goals = Goal.objects.filter(user=request.user, completed=False).order_by('-created_at')[:3]
    return handle_workout_request(request, muscle, recent_workout, incomplete_goals)

@login_required
def bicep_workout(request, muscle):
    recent_workout = WorkoutRecord.objects.filter(user=request.user, workout_type=muscle).order_by('-created_at').first()
    incomplete_goals = Goal.objects.filter(user=request.user, completed=False).order_by('-created_at')[:3]
    return handle_workout_request(request, muscle, recent_workout, incomplete_goals)

@login_required
def tricep_workout(request, muscle):
    recent_workout = WorkoutRecord.objects.filter(user=request.user, workout_type=muscle).order_by('-created_at').first()
    incomplete_goals = Goal.objects.filter(user=request.user, completed=False).order_by('-created_at')[:3]
    return handle_workout_request(request, muscle, recent_workout, incomplete_goals)

@login_required
def delts_workout(request, muscle):
    recent_workout = WorkoutRecord.objects.filter(user=request.user, workout_type=muscle).order_by('-created_at').first()
    incomplete_goals = Goal.objects.filter(user=request.user, completed=False).order_by('-created_at')[:3]
    return handle_workout_request(request, muscle, recent_workout, incomplete_goals)

@login_required
def quads_workout(request, muscle):
    recent_workout = WorkoutRecord.objects.filter(user=request.user, workout_type=muscle).order_by('-created_at').first()
    incomplete_goals = Goal.objects.filter(user=request.user, completed=False).order_by('-created_at')[:3]
    return handle_workout_request(request, muscle, recent_workout, incomplete_goals)

@login_required
def hamstring_workout(request, muscle):
    recent_workout = WorkoutRecord.objects.filter(user=request.user, workout_type=muscle).order_by('-created_at').first()
    incomplete_goals = Goal.objects.filter(user=request.user, completed=False).order_by('-created_at')[:3]
    return handle_workout_request(request, muscle, recent_workout, incomplete_goals)

@login_required
def glutes_workout(request, muscle):
    recent_workout = WorkoutRecord.objects.filter(user=request.user, workout_type=muscle).order_by('-created_at').first()
    incomplete_goals = Goal.objects.filter(user=request.user, completed=False).order_by('-created_at')[:3]
    return handle_workout_request(request, muscle, recent_workout, incomplete_goals)

def save_workout_record(user, muscle, form):
    workout_record = form.save(commit=False)
    workout_record.user = user
    workout_record.username = user.username
    workout_record.workout_type = muscle
    workout_record.save()

def handle_workout_request(request, muscle, recent_workout=None, incomplete_goals=None):
    if request.method == 'POST':
        form = WorkoutRecordForm(request.POST)
        if form.is_valid():
            save_workout_record(request.user, muscle, form)
            return redirect('success_page')
    else:
        form = WorkoutRecordForm()
    return render(request, f'workouts/{muscle}_workout.html', {'form': form, 'recent_workout': recent_workout, 'incomplete_goals': incomplete_goals})


