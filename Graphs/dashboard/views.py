

from django.db.models import Sum
from django.db.models.functions import ExtractMonth
from datetime import date
from .models import Airbooking  
from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

def Graphs(request):
    """
    Calculate the total sum of booking prices for each month of the given year.
    Returns a list of dictionaries containing 'month' (formatted as 'Month') and 'total_price' for each month.
    """
    context={}
    if request.method == 'POST':
        pass
    else:
        year=2023
        monthly_totals = (
            Airbooking.objects
            .filter(Travel_date__year=year,International_trip=False,Is_round=False)  # Filter by the given year (e.g., 2023)
            .annotate(month=ExtractMonth('Travel_date'))
            .values('month')
            .annotate(total_price=Sum('Price'))
            .order_by('month')
        )

        
        # Creating a dictionary to store the total prices by month
        month_totals = {entry['month']: entry['total_price'] for entry in monthly_totals}

        # Creating a list of dictionaries containing 'month' and 'total_price' for all months
        formatted_monthly_totals = []
        for month in range(1, 13):# because range counts n-1
            month_name = date(year, month, 1).strftime('%B') # here its getting the full month name

            total_price = month_totals.get(month, 0) # default value for the months which don't have any amount

            formatted_monthly_totals.append({'month': month_name, 'total_price': total_price})# here we are appending the values for the frontend 

        context['one_way']=formatted_monthly_totals # passing it for the frontend  ! rememeber the context here in bracket can be rendered from frontend.
        # print("format",formatted_monthly_totals)



 ################### for pie charts on the basis of airlines ##################
        flights = (
        Airbooking.objects
        .values('Airline')
        .annotate(total_price=Sum('Price'))
    )
        airline_income = []
        for flight in flights:
            airline_name = flight['Airline']
            total_price = flight['total_price']
            airline_income.append({'Airline': airline_name, 'total_price': total_price})
        




        context['Airlines']=airline_income
        # print(airline_income)


        ########### Chart for tyoe of trip ####
        round_trips = Airbooking.objects.filter(Is_round=True).count()
        International=Airbooking.objects.filter(International_trip=True).count()
        one_way_domestic =Airbooking.objects.filter(Is_round=False,International_trip=False).count()
        one_way_international =Airbooking.objects.filter(Is_round=False,International_trip=False).count()

       
        context[ 'round_trips']= round_trips
        context['International']=International
        context[ 'one_way_domestic']=one_way_domestic
        context['one_way_international']= one_way_international



        airbooking_details=Airbooking.objects.all()
        context['details']=airbooking_details



        return render(request,'dashboard.html',context)
    





