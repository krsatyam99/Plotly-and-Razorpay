
from django.contrib import admin
from django.urls import path
from dashboard import views
from dashboard.views import Graphs



urlpatterns = [
 
    path("Graphs/", views.Graphs)

]
