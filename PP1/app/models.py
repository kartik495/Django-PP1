from django.db import models

# Create your models here.
class Task1(models.Model):
    first=models.CharField(max_length=20)
    last=models.CharField(max_length=20)
    email=models.EmailField(max_length=30)
    password=models.CharField(max_length=50)
    favourite=models.TextField(blank=True)

    def __str__(self):
        return self.first+' '+self.last


