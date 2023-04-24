from rest_framework import serializers
from .models import Person, Task, BadHabit, GoodHabit, GoodHabitToRaise
from django.contrib.auth.models import User
from rest_framework.authtoken.views import Token

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ['id','Name', 'LastName']

class Userserializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username','email', 'password']

        extra_kwargs = {'password':{
            'write_only': True,
            'required': True
        }}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user
    
class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'owner', 'name', 'description', 'priority', 'completed', 'date']
    
class BadHabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = BadHabit
        fields = ['id', 'owner', 'name']

class GoodHabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = GoodHabit
        fields = ['id', 'owner', 'name']

class GoodHabitToRaiseSerializer(serializers.ModelSerializer):
    class Meta:
        model = GoodHabitToRaise
        fields = ['id', 'owner', 'name']