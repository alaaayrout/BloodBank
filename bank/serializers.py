from rest_framework import serializers
from .models import Donor, Patient, Hospital, BloodUnit, Donation, Transfusion

class DonorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Donor
        fields = '__all__'

    def validate_age(self, value):
        if value < 18:
            raise serializers.ValidationError("المتبرع يجب أن يكون عمره 18 سنة أو أكثر.")
        return value

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'

class HospitalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hospital
        fields = '__all__'

class BloodUnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = BloodUnit
        fields = '__all__'

class DonationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Donation
        fields = '__all__'

class TransfusionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transfusion
        fields = '__all__'
