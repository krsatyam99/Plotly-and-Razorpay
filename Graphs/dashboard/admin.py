from django.contrib import admin
from dashboard.models import Airbooking

# # Register your models here.
class Airline_Admin(admin.ModelAdmin):
    list_display = ('id','From', 'To', 'Travel_date','Price','Is_round','International_trip')
admin.site.register(Airbooking,Airline_Admin)
