from pyexpat import model
from re import search
from select import select
from django.contrib import admin
from django.db.models.aggregates import Count,Sum
from django.utils.html import format_html, urlencode
from django.urls import reverse
from . import models

@admin.register(models.Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ['id','first_name', 'last_name','gender','diagnosis','birth_date','personal_code','phone','city', 'appointments_count']
    list_editable = ['gender']
    list_filter = ['diagnosis']
    list_per_page = 10
    ordering = ['first_name','last_name']
    search_fields = ['first_name__istartswith','last_name__istartswith']
    
    @admin.display(ordering='appointments_count')
    def appointments_count(self, patient):
        url=(
            reverse('admin:cabinet_appointment_changelist')
            +'?'
            +urlencode({
                'patient_id':str(patient.id)
            }) )
        return format_html('<a href={}>{}</a>',url, patient.appointments_count)

    def get_queryset(self, request):
        return super().get_queryset(request).annotate(appointments_count=Count('appointment'))


@admin.register(models.Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    autocomplete_fields=['patient']
    list_display = ['id','patient','date','hour', 'confirmation','summary']
    list_editable = ['confirmation']
    list_filter = ['date', 'confirmation']
    list_per_page = 10
    search_fields = ['patient__last_name__istartswith']
   

@admin.register(models.Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['id','title','price']
    list_editable = ['price']
    

class ServiceItemInline(admin.TabularInline):
    model = models.ServiceItem


@admin.register(models.Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    autocomplete_fields=['patient']
    list_display = ['created_at','patient', 'total_price' ]
    list_per_page = 10
    inlines = [ServiceItemInline]
    
    def total_price(self, invoice):
        return invoice.total_price

    def get_queryset(self, request):
        return super().get_queryset(request).annotate(total_price=Sum('serviceitems__price')) 


    



    
  
    
  

   