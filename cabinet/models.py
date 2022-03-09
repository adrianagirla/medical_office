from asyncio.windows_events import NULL
from enum import unique
from pyexpat import model
from tkinter import CASCADE
from tkinter.tix import TCL_DONT_WAIT
from django.db import models
from django.contrib import admin
from django.conf import settings
from django.core.validators import MinLengthValidator
from django.conf import settings

class Patient(models.Model):
    Gender_female = 'F'
    Gender_male = "M"
    Gender_nonbinary = 'N-B'
    Gender_choices = [(Gender_female, 'Female'),
                      (Gender_male, 'Male'),
                      (Gender_nonbinary, 'Non-binary')]
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    birth_date = models.DateField(null=True)
    personal_code = models.CharField(max_length=13,
                                     validators=[MinLengthValidator(13)] )
    phone = models.CharField(max_length=10)
    city = models.CharField(max_length=50)
    district = models.CharField(max_length=50)
    diagnosis = models.CharField(max_length=255)
    gender = models.CharField(max_length=3, choices=Gender_choices, default=Gender_female)

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'

    class Meta:
        ordering = ['first_name','last_name']

    
class Appointment(models.Model):
    Confirmation_affirmative = 'Y'
    Confirmation_negative = "N"
    Confirmation_choices = [(Confirmation_affirmative, 'Yes'),
                            (Confirmation_negative, 'No')]
    date = models.DateField(null=True)
    hour = models.TimeField(null=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    confirmation = models.CharField(max_length=1, choices=Confirmation_choices, default=Confirmation_negative)
    summary = models.TextField(null=True)
    
    def __str__(self) -> str:
        return super().__str__()


class Service(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
 
    def __str__(self) -> str:
        return self.title   

  
class Invoice(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    patient = models.ForeignKey(Patient, on_delete=models.PROTECT)

    def __str__(self) -> str:
        return  super().__str__()
    

class ServiceItem(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE, null=True, related_name='serviceitems')
    service = models.ForeignKey(Service, on_delete=models.CASCADE, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self) -> str:
        return super().__str__()




