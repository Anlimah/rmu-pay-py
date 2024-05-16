# customer_management/models.py
from django.db import models

class Customer(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    gender = models.CharField(max_length=15)
    created = models.DateTimeField(auto_now_add=True)

class NotificationSettings(models.Model):
    customer = models.OneToOneField(Customer, on_delete=models.CASCADE)
    sms_enabled = models.BooleanField(default=False)
    email_enabled = models.BooleanField(default=False)
    inapp_enabled = models.BooleanField(default=False)
