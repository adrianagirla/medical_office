from dataclasses import field, fields
from rest_framework import serializers
from .models import Patient, Appointment, Service, ServiceItem, Invoice

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model= Patient
        fields= ['id','first_name', 'last_name','gender','diagnosis','birth_date','personal_code','phone','email','city','district', 'appointments_count']  
    appointments_count = serializers.IntegerField(read_only=True)


class SimplePatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ['first_name', 'last_name', 'personal_code']


class AppointmentSerializer(serializers.ModelSerializer):
    patient = SimplePatientSerializer()
    class Meta:
        model = Appointment
        fields = ['id','patient','date','hour', 'confirmation', 'summary']


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ['id','title', 'price']


class ServiceItemSerializer(serializers.ModelSerializer):
    service =ServiceSerializer()
    class Meta:
        model = ServiceItem
        fields = ['id','service', 'price']


class InvoiceSerializer(serializers.ModelSerializer):
    serviceitems = ServiceItemSerializer(many=True)
    patient = SimplePatientSerializer()
    class Meta:
        model = Invoice
        fields = ['id','patient','created_at','total_price', 'serviceitems']
        
    total_price = serializers.IntegerField(read_only=True)


    
