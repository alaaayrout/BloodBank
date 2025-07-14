from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse 

from rest_framework.routers import DefaultRouter
from bank.views import DonorViewSet, PatientViewSet, BloodUnitViewSet, DonationViewSet, TransfusionViewSet


router = DefaultRouter()
router.register(r'donors', DonorViewSet)
router.register(r'patients', PatientViewSet)
router.register(r'blood-units', BloodUnitViewSet)
router.register(r'donations', DonationViewSet)
router.register(r'transfusions', TransfusionViewSet)


def home_view(request):
    return HttpResponse("""
        <h1>مرحباً بك في نظام بنك الدم 🩸</h1>
        <p>للدخول إلى الواجهات البرمجية، اذهب إلى <a href="/api/">/api/</a></p>
    """)


                     
urlpatterns = [
    path('', home_view),   
    path('admin/', admin.site.urls),
    path('api/', include('bank.urls')),
]
