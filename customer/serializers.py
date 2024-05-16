# customer_management/serializers.py
from rest_framework import serializers
from .models import Customer, NotificationSettings

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

class NotificationSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = NotificationSettings
        fields = ['sms_enabled', 'email_enabled', 'inapp_enabled', 'customer']
        read_only_fields = ['customer']

