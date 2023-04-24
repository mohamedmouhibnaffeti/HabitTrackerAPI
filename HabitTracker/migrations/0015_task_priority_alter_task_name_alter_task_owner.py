# Generated by Django 4.1.7 on 2023-04-09 00:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HabitTracker', '0014_task_cancelled'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='priority',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AlterField(
            model_name='task',
            name='name',
            field=models.CharField(default='', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='owner',
            field=models.CharField(default='', max_length=30, null=True),
        ),
    ]
