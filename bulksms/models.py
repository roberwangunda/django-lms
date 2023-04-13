from twilio.rest import Client
from django.db import models 
from phone_field import PhoneField
from accounts.models import *

# class Student(models.Model):
#         numbers = Student.objects.values_list('phone')
#         def _str_(self):

#             return str(self.numbers)


#defining a simple classc
class Messages(models.Model):
    recipient= models.ForeignKey(Parent,null=True,on_delete=models.CASCADE)
    message = models.CharField(max_length=2000)

#string representation
    def _str_(self):
        return f"{self.message}"
        

    #save method
    def save(self, *args, **kwargs):
        numbers = Parent.objects.values_list('phone')
        
        account_sid = "AC02fc473179027d8013486d90912ed465"
        auth_token = 'cfb3d6790081f1714a92c9515003aa83'
        client = Client(account_sid, auth_token)
        for number in numbers:
            print(number)
            message = client.messages.create(
            to = number,
            body=f"{self.message}",
            from_ ="+15677071083")
        return super().save(*args, **kwargs)