from django.db import models

class Activity(models.Model):
    name = models.CharField(max_length=200, verbose_name="Activity Name")
    date = models.DateField(verbose_name="Date")
    time = models.TimeField(verbose_name="Time")
    description = models.TextField(verbose_name="Description", blank=True)

    def __str__(self):
        return self.name
