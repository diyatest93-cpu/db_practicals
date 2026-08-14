from django.db import models

# Create your models here.
class Image(models.Model):
    image = models.ImageField(upload_to='images/')
    name = models.CharField(max_length=100, blank=True)
    size = models.CharField(max_length=100, blank=True)


class save_info(models.Model):
    GENDER_CHOICES=[
        ("male", "Male"),
        ("female", "female")
    ]
    CITY_CHOICES=[
        ('hmt', 'himmatnagar'),
        ('idar', 'idar'),
        ('surat', 'surat')
    ]
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=20)
    gender=models.CharField(max_length=10,choices= GENDER_CHOICES)
    city=models.CharField(max_length=10,choices=CITY_CHOICES)
        