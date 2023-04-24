from django.contrib import admin
from .models import Person, Task, BadHabit, GoodHabit, GoodHabitToRaise
# Register your models here.
@admin.register(Person)
class PersonModel( admin.ModelAdmin):
    list_display = ('Name', 'LastName')

@admin.register(Task)
class TaskModel( admin.ModelAdmin):
    Tasks_display  = ('Title', 'Creator')

@admin.register(BadHabit)
class BadHabitModel( admin.ModelAdmin):
    Bad_Habits_display  = ('name', 'owner')

@admin.register(GoodHabit)
class GoodHabitModel( admin.ModelAdmin):
    Good_Habits_display  = ('name', 'owner')

@admin.register(GoodHabitToRaise)
class GoodHabitToRaiseModel( admin.ModelAdmin):
    Good_Habits_To_Raise_display  = ('name', 'owner')
