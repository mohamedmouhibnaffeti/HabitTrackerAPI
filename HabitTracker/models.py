from django.db import models
import os
from twilio.rest import Client
# Create your models here.


class Person(models.Model):
    Name = models.CharField(max_length=30)
    LastName = models.CharField(max_length=30)

class Task(models.Model):
    owner = models.CharField(max_length=30, default="", null=True)
    name = models.CharField(max_length=50,default="", null=True)
    description = models.TextField(null=True)
    priority = models.CharField(max_length=30,default="None")
    completed = models.BooleanField(default=False)
    date = models.DateTimeField()
class BadHabit(models.Model):
    owner = models.CharField(max_length=30, default="", null=True)
    name = models.CharField(max_length=30, default="")

class GoodHabit(models.Model):
    owner = models.CharField(max_length=30, default="", null=True)
    name = models.CharField(max_length=30, default="")


class GoodHabitToRaise(models.Model):
    owner = models.CharField(max_length=30, default="", null=True)
    name = models.CharField(max_length=30, default="")


"""
    def is_overdue(self):
        return self.date < timezone.now() and self.completed == False 

    def send_overdue_message(self):
        # Your Nexmo API key and secret
        api_key = "681b57fb"
        api_secret = "gHoGlquaUTmNt3vY"
        # Your Nexmo virtual phone number
        nexmo_phone_number = "21692144354"
        # Recipient's phone number in international format without leading '+'
        recipient_phone_number = "+21628056362"

        if self.is_overdue():
            client = nexmo.Client(key=api_key, secret=api_secret)
            message = {
                "from": nexmo_phone_number,
                "to": recipient_phone_number,
                "text": f"The task '{self.name}' is overdue!"
            }
            response = client.send_message(message)

            if response["messages"][0]["status"] == "0":
                print(f"Sent SMS message '{response['messages'][0]['message-id']}' to {recipient_phone_number}")
            else:
                print(f"Failed to send SMS message to {recipient_phone_number}")
for task in Task.objects.all():
    task.send_overdue_message()
        
"""