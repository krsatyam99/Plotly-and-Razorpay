
from django.contrib import admin
from django.urls import path
from Payment_gateways import views
from Payment_gateways.views import razorpay





urlpatterns = [
 
    path("razorpay/", views.razorpay)

]
