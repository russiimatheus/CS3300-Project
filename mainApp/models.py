from django.db import models
from django.utils.translation import gettext_lazy as _
from django.conf import settings

class Activity(models.Model):
    name = models.CharField(max_length=200, verbose_name=_("Activity Name"))
    date = models.DateField(verbose_name=_("Date"))
    time = models.TimeField(verbose_name=_("Time"))
    description = models.TextField(verbose_name=_("Description"), blank=True)

    MATHEUS = 'Matheus'
    MATIAS = 'Matias'
    MATHEUSES = 'Matheuses'
    INSTRUCTOR_CHOICES = [
        (MATHEUS, _('Matheus')),
        (MATIAS, _('Matias')),
        (MATHEUSES, _('Matheuses')),
    ]

    instructor = models.CharField(
        max_length=15,
        choices=INSTRUCTOR_CHOICES,
        default=MATHEUS,
        verbose_name=_("Instructor")
    )

    def __str__(self):
        return self.name

class Registration(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} - {self.activity.name}"
