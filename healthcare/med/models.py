from django.db import models

# Create your models here.
class Doctor(models.Model):
    Name = models.CharField(max_length=50)
    mobile = models.IntegerField()
    specialites = models.CharField(max_length=20)

class Patient(models.Model):
    Name = models.CharField(max_length=20)
    gender = models.CharField(max_length=10)
    mobile = models.IntegerField()
    address = models.TextField()

class Appointment(models.Model):
    doctor = models.ForeignKey(Doctor,on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient,on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()

