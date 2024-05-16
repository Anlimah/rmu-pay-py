from django.http import Http404
from django.shortcuts import render
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import generics, mixins, status
from .models import Customer, NotificationSettings
from .serializers import CustomerSerializer, NotificationSettingsSerializer

class CustomerListCreateAPIView(
    generics.GenericAPIView, 
    mixins.CreateModelMixin, 
    mixins.ListModelMixin
):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    def get(self, request:Request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request:Request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class CustomerDetailAPIView(
    generics.GenericAPIView, 
    mixins.RetrieveModelMixin, 
    mixins.UpdateModelMixin, 
    mixins.DestroyModelMixin
):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    def get(self, request:Request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request:Request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request:Request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

class NotificationSettingsDetailAPIView(
    generics.GenericAPIView,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin
):
    queryset = NotificationSettings.objects.all()
    serializer_class = NotificationSettingsSerializer

    def get_object(self, customer_id):
        try:
            return NotificationSettings.objects.get(customer_id=customer_id)
        except NotificationSettings.DoesNotExist:
            raise Http404

    def get(self, request:Request, customer_id):
        notification_setting = self.get_object(customer_id)
        serializer = self.serializer_class(notification_setting)
        return Response(serializer.data)
    
    def post(self, request, customer_id):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save(customer_id=customer_id)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request:Request, customer_id):
        notification_setting = self.get_object(customer_id)
        serializer = self.serializer_class(notification_setting, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request:Request, customer_id):
        notification_setting = self.get_object(customer_id)
        notification_setting.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)