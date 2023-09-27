from django.db import models


# Choices for Airline
AIRLINE_CHOICES = (
    ('Air_India', 'Air India'),
    ('Indigo', 'Indigo'),
    ('Spicejet', 'Spicejet'),
    ('Go_Air', 'Go Air'),
    ('Vistara', 'Vistara'),
)

# Choices for Travel_type
CLASS_TYPE_CHOICES = (
    ('first_class', 'First Class'),
    ('economy_class', 'Economy Class'),
    ('business_class', 'Business Class'),
)

class Airbooking(models.Model):
    From = models.CharField(null=True, max_length=100)
    To = models.CharField(null=True, max_length=100)
    booking_date = models.DateTimeField(null=True)
    Travel_date = models.DateTimeField(null=True)
    Is_round = models.BooleanField(null=True, default=False)
    Round_from = models.CharField(null=True, max_length=100, blank=True)
    round_To = models.CharField(null=True, max_length=100, blank=True)
    round_travel_date = models.DateTimeField(null=True, blank=True)
    Airline = models.CharField(max_length=100, choices=AIRLINE_CHOICES, default="none")
    Travel_type = models.CharField(max_length=100, choices=CLASS_TYPE_CHOICES, default="none")
    No_of_passeengers = models.IntegerField(default=1)
    Price = models.IntegerField(null=True)
    International_trip = models.BooleanField(default=False)
    def save(self, *args, **kwargs):
            if self.Is_round:
                self.Round_from = self.To
                self.round_To = self.From
            super(Airbooking, self).save(*args, **kwargs)
        

    def __str__(self):
        return f"Booking from {self.From} to {self.To} on {self.Travel_date}"
