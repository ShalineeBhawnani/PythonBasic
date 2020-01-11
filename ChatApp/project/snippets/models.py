from django.core.cache import cache 
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
from django.db import models
from django import forms

class Registration(models.Model):
    
    fullname = models.CharField(max_length = 100)
    username = models.CharField(max_length = 100)
    email = models.EmailField()
    password = models.CharField(max_length = 100)

    if fullname == "" or username == "" or email == "" or password == "":
        raise forms.ValidationError(" one of the above field is empty")

    def __str__(self):
        return self.id

