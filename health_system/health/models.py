from django.db import models
from django.contrib.auth.models import User

class HealthProgram(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Client(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    programs = models.ManyToManyField(HealthProgram, related_name='clients', blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"




class DoctorProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.CharField(max_length=100)
    employee_number = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return f"Profile of {self.user.username}"

    def get_full_name(self):
        return f"{self.user.first_name} {self.user.last_name}"
