# Generated by Django 4.2.5 on 2023-10-25 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='instructor',
            field=models.CharField(choices=[('Matheus', 'Matheus'), ('Matias', 'Matias'), ('Matheuses', 'Matheuses')], default='Matheus', max_length=15, verbose_name='Instructor'),
        ),
    ]