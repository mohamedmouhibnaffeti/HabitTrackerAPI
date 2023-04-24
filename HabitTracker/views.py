from rest_framework.decorators import action, authentication_classes, permission_classes
from django.shortcuts import render
from .models import Person, Task, BadHabit, GoodHabit, GoodHabitToRaise
from .serializers import PersonSerializer, Userserializer, TaskSerializer, BadHabitSerializer, GoodHabitSerializer, GoodHabitToRaiseSerializer
from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
# Create your views here.

def index(request):
    return(render(request, 'index.html'))

class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = (TokenAuthentication,)

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = Userserializer
   
class TasksViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class BadHabitViewSet(viewsets.ModelViewSet):
    queryset = BadHabit.objects.all()
    serializer_class = BadHabitSerializer

class GoodHabitViewSet(viewsets.ModelViewSet):
    queryset = GoodHabit.objects.all()
    serializer_class = GoodHabitSerializer

class GoodHabitToRaiseViewSet(viewsets.ModelViewSet):
    queryset = GoodHabitToRaise.objects.all()
    serializer_class = GoodHabitToRaiseSerializer
