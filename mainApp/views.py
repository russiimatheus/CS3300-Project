from django.shortcuts import render, redirect, get_object_or_404
from .models import Activity
from .forms import ActivityEditForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def index(request):
    return render(request, 'index.html')

def view_activities(request):
    activities = Activity.objects.all()
    context = {'activities': activities}
    return render(request, 'view_activities.html', context)

@login_required
def create_activity(request):
    if request.method == "POST":
        activity_name = request.POST['activity_name']
        activity_date = request.POST['activity_date']
        activity_time = request.POST['activity_time']
        activity_description = request.POST.get('activity_description', '')
        activity_instructor = request.POST['instructor']

        activity = Activity(name=activity_name, date=activity_date, time=activity_time, description=activity_description, instructor=activity_instructor)
        activity.save()

        return redirect('view_activities')

    return render(request, 'create_activity.html')

@login_required
def edit_activity(request, activity_id):
    activity = get_object_or_404(Activity, pk=activity_id)
    
    if request.method == "POST":
        form = ActivityEditForm(request.POST, instance=activity)
        
        if form.is_valid():
            form.save()
            return redirect('view_activities')
    else:
        form = ActivityEditForm(instance=activity)

    return render(request, 'edit_activities.html', {'form': form, 'activity': activity})

@login_required
def delete_activity(request, activity_id):
    activity = get_object_or_404(Activity, pk=activity_id)
    
    if request.method == "POST":
        activity.delete()
        return redirect('view_activities')
    
    return render(request, 'confirm_delete.html', {'activity': activity})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration successful. You can now log in.')
            return redirect('login')
        else:
            for field in form:
                for error in field.errors:
                    messages.error(request, f"{field.label}: {error}")
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def learn_more(request):
    pass

def contact_support(request):
    pass

def school_website(request):
    pass
