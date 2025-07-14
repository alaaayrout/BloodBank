from django.db import models
from django.contrib.auth.models import User

GENDER_CHOICES = [
    ('M', 'ذكر'),
    ('F', 'أنثى'),
]

BLOOD_TYPE_CHOICES = [
    ('A+', 'A+'),
    ('A-', 'A-'),
    ('B+', 'B+'),
    ('B-', 'B-'),
    ('AB+', 'AB+'),
    ('AB-', 'AB-'),
    ('O+', 'O+'),
    ('O-', 'O-'),
]

ROLE_CHOICES = [
    ('donor', 'متبرع'),
    ('patient', 'مريض'),
    ('nurse', 'ممرض'),
    ('manager', 'مدير'),
]

class Profile(models.Model):
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)

    def __str__(self):
        return self.role

class Donor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    age = models.IntegerField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    blood_type = models.CharField(max_length=3, choices=BLOOD_TYPE_CHOICES)
    contact_info = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username if self.user else "No user"

class Patient(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    age = models.IntegerField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    blood_type = models.CharField(max_length=3, choices=BLOOD_TYPE_CHOICES)

    def __str__(self):
        return self.user.username if self.user else "No user"

class DonationAppointment(models.Model):
    donor = models.ForeignKey(Donor, on_delete=models.CASCADE)
    appointment_date = models.DateTimeField()
    location = models.CharField(max_length=100)

    def __str__(self):
        return f"Appointment for {self.donor.user.username} on {self.appointment_date}"

class BloodUnit(models.Model):
    blood_type = models.CharField(max_length=3, choices=BLOOD_TYPE_CHOICES)
    quantity = models.IntegerField()
    donation_date = models.DateField()
    donor = models.ForeignKey(Donor, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.blood_type} - {self.quantity} units"

class Donation(models.Model):
    donor = models.ForeignKey(Donor, on_delete=models.CASCADE)
    blood_unit = models.ForeignKey(BloodUnit, on_delete=models.CASCADE)
    nurse = models.ForeignKey(User, on_delete=models.CASCADE)
    donation_date = models.DateField()

    def __str__(self):
        return f"Donation by {self.donor.user.username}"

class MedicalNote(models.Model):
    donation = models.OneToOneField(Donation, on_delete=models.CASCADE)
    nurse = models.ForeignKey(User, on_delete=models.CASCADE)
    note = models.TextField()

    def __str__(self):
        return f"Note for donation {self.donation.id}"

class Transfusion(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    blood_unit = models.ForeignKey(BloodUnit, on_delete=models.CASCADE)
    nurse = models.ForeignKey(User, on_delete=models.CASCADE)
    transfusion_date = models.DateField()
    receptionist = models.ForeignKey(User, on_delete=models.CASCADE, related_name='receptionist_transfusions')
    accountant = models.ForeignKey(User, on_delete=models.CASCADE, related_name='accountant_transfusions')

    def __str__(self):
        return f"Transfusion for {self.patient.user.username}"
