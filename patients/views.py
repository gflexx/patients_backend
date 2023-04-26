from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import *

class PatientsListApiView(GenericAPIView):
    """
    creates and lists patients
    """
    
    serializer_class = PatientsSerializer

    def get(self, request, *args, **kwargs):
        patients = Patients.objects.all()
        serializer = PatientsSerializer(patients, many=True)
        return Response(serializer.data)
    
    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = PatientsSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else: 
            data = {
                    "status": "failed",
                    "message": serializer.errors
                }
            return Response(data, status=status.HTTP_400_BAD_REQUEST)

class PatientRecordsListApiView(GenericAPIView):
    """
    creates and lists patient records
    """

    serializer_class = PatientRecordsSerializer

    def get(self, request, *args, **kwargs):
        records = PatientRecords.objects.all()
        serializer = PatientRecordsSerializer(records, many=True)
        return Response(serializer.data)
    
    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = PatientRecordsSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else: 
            data = {
                    "status": "failed",
                    "message": serializer.errors
                }
            return Response(data, status=status.HTTP_400_BAD_REQUEST)