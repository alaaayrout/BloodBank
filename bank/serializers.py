from rest_framework import serializers
from .models import (
    Donor, Patient, BloodUnit,
    Donation, Transfusion, Profile,
    DonationAppointment, MedicalNote
)
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'

class DonorSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Donor
        fields = '__all__'

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = User.objects.create_user(**user_data)
        return Donor.objects.create(user=user, **validated_data)

class PatientSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Patient
        fields = '__all__'

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = User.objects.create_user(**user_data)
        return Patient.objects.create(user=user, **validated_data)

class BloodUnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = BloodUnit
        fields = '__all__'

class DonationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Donation
        fields = '__all__'

class MedicalNoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalNote
        fields = '__all__'

class DonationAppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = DonationAppointment
        fields = '__all__'

class TransfusionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transfusion
        fields = '__all__'
