from django import forms
from .models import Activity

class ActivityEditForm(forms.ModelForm):
    class Meta:
        model = Activity
        fields = ['name', 'date', 'time', 'description']  # You can specify any fields you want to be editable.
