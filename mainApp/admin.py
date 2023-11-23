from django.contrib import admin
from .models import Activity
from django.utils.translation import gettext_lazy as _


@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ['name', 'date', 'time', 'instructor']
    list_filter = ['date', 'instructor']
    search_fields = ['name', 'description']
