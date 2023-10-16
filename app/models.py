from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django import forms

class Psychologist(models.Model):
    fname = models.CharField(max_length=30)
    lname = models.CharField(max_length=30)
    category = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)])
    experience = models.IntegerField()
    hour_price = models.IntegerField(null=True)
    
    def __str__(self):
        return self.fname + " " + self.lname

class Appointment(models.Model):
    client_fname = models.CharField(max_length=30)
    client_lname = models.CharField(max_length=30)
    date = models.DateField()
    time = models.CharField(max_length=10)
    psychologist = models.ForeignKey("Psychologist", verbose_name=("Психолог"), on_delete=models.CASCADE)
    
    def __str__(self):
        return self.client_fname + " " + self.client_lname