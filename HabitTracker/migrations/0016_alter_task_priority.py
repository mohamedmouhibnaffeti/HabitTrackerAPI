# Generated by Django 4.1.7 on 2023-04-09 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HabitTracker', '0015_task_priority_alter_task_name_alter_task_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='priority',
            field=models.CharField(default='None', max_length=30),
        ),
    ]
