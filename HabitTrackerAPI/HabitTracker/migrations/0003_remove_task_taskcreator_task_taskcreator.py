# Generated by Django 4.1.7 on 2023-03-25 12:37

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('HabitTracker', '0002_task'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='Taskcreator',
        ),
        migrations.AddField(
            model_name='task',
            name='Taskcreator',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
