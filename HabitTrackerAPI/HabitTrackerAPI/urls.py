from django.contrib import admin
from django.urls import path, include
from HabitTracker.views import index
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('HabitTracker.urls')),
    path('index/',index, name='index'),
]
