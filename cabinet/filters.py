from dataclasses import field, fields
from django_filters.rest_framework import FilterSet
from .models import Appointment, Patient

class AppointmentFilter(FilterSet):
    class Meta:
        model = Appointment
        fields = {
            'patient_id':['exact'],
            'date':['exact', 'year__gt'],
            }

class PatientFilter(FilterSet):
    class Meta:
        model = Patient
        fields = {
            'birth_date':['exact', 'year__gt','year__lt'],
            'gender':['exact'],
            'city':['exact'],
            'diagnosis':['exact'],
        }