from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    PATIENT = 'PATIENT'
    DOCTOR = 'DOCTOR'
    PHARMACIST = 'PHARMACIST'
    DELIVERY  = 'DELIVERY'

    ROLE_CHOICES = (
        (PATIENT, 'Patient'),
        (DOCTOR, 'Doctor'),
        (PHARMACIST, 'Pharmacist'),
        (DELIVERY, 'Delivery')
    )

    profile_photo = models.ImageField()
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default=PATIENT)