
from django.contrib import admin
from .models import Donor, Patient, BloodUnit, Donation, Transfusion

admin.site.register(Donor)
admin.site.register(Patient)
admin.site.register(BloodUnit)
admin.site.register(Donation)
admin.site.register(Transfusion)
# Register your models here.
