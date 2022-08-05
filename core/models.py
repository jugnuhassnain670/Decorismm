from django.db import models

# Create your models here.
class NewsLetter(models.Model):
    email=models.CharField(max_length=255)
    
    def __str__(self):
        return self.email


class ContactUs(models.Model):
    name=models.CharField(max_length=255)
    email=models.CharField(max_length=255)
    message = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name