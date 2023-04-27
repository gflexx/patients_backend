from django.db import models

GENDER_CHOICES = (
    ("male", "Male"),
    ("female", "Female"),
    ("other", "Other")
)

HEALTH_CHOICES = (
    ("good", "Good"),
    ("poor", "Poor")
)


class Patients(models.Model):
    first_name = models.CharField(max_length=108)
    last_name = models.CharField(max_length=108)
    dob = models.DateField()
    gender = models.CharField(
        choices=GENDER_CHOICES, 
        max_length=8
    )
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']
        verbose_name_plural = 'Patients'

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class PatientRecords(models.Model):
    patient = models.ForeignKey(
        Patients,
        on_delete=models.CASCADE,
    )
    date = models.DateField()
    height = models.IntegerField()
    weight = models.IntegerField()
    bmi = models.IntegerField()
    general_health = models.CharField(
        choices=HEALTH_CHOICES, 
        max_length=6, 
        blank=True,
        null=True
    )
    taking_drugs = models.BooleanField(null=True, blank=True)
    comments = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    class Meta:
        ordering = ['-created']
        verbose_name_plural = 'Patient Records'