from django.db import models

# Create your models here.
class save_info(models.Model):
    CITY_CHOICES=[
        ('hmt', 'Himmatnagar'),
        ('idar', 'Idar'),
        ('surat', 'Surat'),
    ]
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    mobileNo=models.CharField(max_length=12)
    gender=models.CharField(max_length=10)
    city=models.CharField(max_length=20, choices=CITY_CHOICES)

    def __str__(self):
       return self.name







