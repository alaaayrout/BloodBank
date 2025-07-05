from django.shortcuts import render
from rest_framework import viewsets
from .models import Donor, Patient, Hospital, BloodUnit, Donation, Transfusion
from .serializers import DonorSerializer, PatientSerializer, HospitalSerializer, BloodUnitSerializer, DonationSerializer, TransfusionSerializer

class DonorViewSet(viewsets.ModelViewSet):
    queryset = Donor.objects.all()
    serializer_class = DonorSerializer

class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

class HospitalViewSet(viewsets.ModelViewSet):
    queryset = Hospital.objects.all()
    serializer_class = HospitalSerializer

class BloodUnitViewSet(viewsets.ModelViewSet):
    queryset = BloodUnit.objects.all()
    serializer_class = BloodUnitSerializer

class DonationViewSet(viewsets.ModelViewSet):
    queryset = Donation.objects.all()
    serializer_class = DonationSerializer

class TransfusionViewSet(viewsets.ModelViewSet):
    queryset = Transfusion.objects.all()
    serializer_class = TransfusionSerializer


