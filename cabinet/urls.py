from django.db import router
from django.urls import path
from . import views
from rest_framework.routers import  DefaultRouter

router = DefaultRouter()

router.register('patients', views.PatientViewSet)
router.register('appointments', views.AppointmentViewSet)
router.register('services', views.ServiceViewSet)
router.register('invoices', views.InvoiceViewSet)


urlpatterns = router.urls
