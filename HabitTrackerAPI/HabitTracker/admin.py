from django.contrib import admin
from .models import Person, Task
# Register your models here.
@admin.register(Person)
class PersonModel( admin.ModelAdmin):
    list_display = ('Name', 'LastName')

@admin.register(Task)
class TaskModel( admin.ModelAdmin):
    Tasks_display  = ('Title', 'Creator')

