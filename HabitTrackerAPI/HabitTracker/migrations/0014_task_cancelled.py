# Generated by Django 4.1.7 on 2023-03-30 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HabitTracker', '0013_alter_task_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='cancelled',
            field=models.BooleanField(default=False),
        ),
    ]