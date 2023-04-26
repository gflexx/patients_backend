from rest_framework import serializers

from .models import *

class PatientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patients
        fields = "__all__"

class PatientRecordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientRecords
        fields = "__all__"

    def to_representation(self, instance):
        self.fields['patient'] = PatientsSerializer(read_only=True)
        return super(PatientRecordsSerializer, self).to_representation(instance)