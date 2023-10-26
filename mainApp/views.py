from django.shortcuts import render, redirect, get_object_or_404
from .models import Activity
from .forms import ActivityEditForm

def index(request):
    return render(request, 'index.html')

def view_activities(request):
    activities = Activity.objects.all()
    context = {'activities': activities}
    return render(request, 'view_activities.html', context)

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

def delete_activity(request, activity_id):
    activity = get_object_or_404(Activity, pk=activity_id)
    
    if request.method == "POST":
        activity.delete()
        return redirect('view_activities')
    
    return render(request, 'confirm_delete.html', {'activity': activity})


# ... other views ...

def learn_more(request):
    pass

def contact_support(request):
    pass

def school_website(request):
    pass
