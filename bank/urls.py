from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'donors', DonorViewSet)
router.register(r'patients', PatientViewSet)
router.register(r'blood-units', BloodUnitViewSet)
router.register(r'donations', DonationViewSet)
router.register(r'transfusions', TransfusionViewSet)
router.register(r'profiles', ProfileViewSet)
router.register(r'appointments', DonationAppointmentViewSet)
router.register(r'medical-notes', MedicalNoteViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
