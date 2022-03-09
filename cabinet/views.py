from re import search
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models.aggregates import Count,Sum
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter, OrderingFilter
from .models import Appointment, Patient, Invoice, Service
from .serializers import PatientSerializer, AppointmentSerializer, InvoiceSerializer, ServiceSerializer, ServiceItemSerializer
from .filters import AppointmentFilter, PatientFilter



class PatientViewSet(ModelViewSet):
        queryset = Patient.objects.annotate(appointments_count=Count('appointment'))
        serializer_class = PatientSerializer 
        filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
        filterset_class = PatientFilter
        search_fields = ['first_name', 'last_name', 'personal_code', 'phone', 'diagnosis']
        ordering_fields = ['last_name', 'first_name']

        def get_serializer_context(self):
            return {'request': self.request}
  

class AppointmentViewSet(ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = AppointmentFilter
    search_fields = ['patient']
    ordering_fields = ['date']

    def get_serializer_context(self):
            return {'request': self.request}


class ServiceViewSet(ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

    def get_serializer_context(self):
            return {'request': self.request}


class InvoiceViewSet(ModelViewSet):
    queryset = Invoice.objects.annotate(total_price=Sum('serviceitems__price'))
    serializer_class = InvoiceSerializer

    def get_serializer_context(self):
            return {'request': self.request}




