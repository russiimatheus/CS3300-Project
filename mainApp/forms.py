from django import forms
from .models import Activity
from django.utils.translation import gettext_lazy as _


class ActivityEditForm(forms.ModelForm):
    class Meta:
        model = Activity
        fields = ['name', 'date', 'time', 'description', 'instructor']
        labels = {
            'name': _('Name'),
            'date': _('Date'),
            'time': _('Time'),
            'description': _('Description'),
            'instructor': _('Instructor'),
        }
