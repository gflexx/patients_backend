from django.urls import path

from .views import *

urlpatterns = [
    path('patients/', PatientsListApiView.as_view()),
    path('records/', PatientRecordsListApiView.as_view())
]