from rest_framework import viewsets
from .models import (
    Donor, Patient, BloodUnit,
    Donation, Transfusion, Profile,
    DonationAppointment, MedicalNote
)
from .serializers import (
    DonorSerializer, PatientSerializer, BloodUnitSerializer,
    DonationSerializer, TransfusionSerializer, ProfileSerializer,
    DonationAppointmentSerializer, MedicalNoteSerializer
)

class DonorViewSet(viewsets.ModelViewSet):
    queryset = Donor.objects.all()
    serializer_class = DonorSerializer

class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

class BloodUnitViewSet(viewsets.ModelViewSet):
    queryset = BloodUnit.objects.all()
    serializer_class = BloodUnitSerializer

class DonationViewSet(viewsets.ModelViewSet):
    queryset = Donation.objects.all()
    serializer_class = DonationSerializer

class TransfusionViewSet(viewsets.ModelViewSet):
    queryset = Transfusion.objects.all()
    serializer_class = TransfusionSerializer

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class DonationAppointmentViewSet(viewsets.ModelViewSet):
    queryset = DonationAppointment.objects.all()
    serializer_class = DonationAppointmentSerializer

class MedicalNoteViewSet(viewsets.ModelViewSet):
    queryset = MedicalNote.objects.all()
    serializer_class = MedicalNoteSerializer
