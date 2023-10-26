from django.db import models

class Activity(models.Model):
    name = models.CharField(max_length=200, verbose_name="Activity Name")
    date = models.DateField(verbose_name="Date")
    time = models.TimeField(verbose_name="Time")
    description = models.TextField(verbose_name="Description", blank=True)

    # New Instructor field
    MATHEUS = 'Matheus'
    MATIAS = 'Matias'
    MATHEUSES = 'Matheuses'
    INSTRUCTOR_CHOICES = [
        (MATHEUS, 'Matheus'),
        (MATIAS, 'Matias'),
        (MATHEUSES, 'Matheuses'),
    ]

    instructor = models.CharField(
        max_length=15,
        choices=INSTRUCTOR_CHOICES,
        default=MATHEUS,  # Set a default instructor as "Matheus"
        verbose_name="Instructor"
    )

    def __str__(self):
        return self.name
