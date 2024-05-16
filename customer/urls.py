# customer_management/urls.py
from django.urls import path
from .views import CustomerListCreateAPIView, CustomerDetailAPIView, NotificationSettingsDetailAPIView

urlpatterns = [
    path('', CustomerListCreateAPIView.as_view(), name='customer-list-create'),
    path('<int:pk>', CustomerDetailAPIView.as_view(), name='customer-detail'),
    path('<int:customer_id>/notification-settings/', NotificationSettingsDetailAPIView.as_view(), name='notification-settings-detail'),
]
