# Generated by Django 4.2.5 on 2023-09-24 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Airbooking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('From', models.CharField(max_length=100, null=True)),
                ('To', models.CharField(max_length=100, null=True)),
                ('booking_date', models.DateTimeField(null=True)),
                ('Travel_date', models.DateTimeField(null=True)),
                ('Is_round', models.BooleanField(default=False, null=True)),
                ('Round_from', models.CharField(max_length=100, null=True)),
                ('round_To', models.CharField(max_length=100, null=True)),
                ('round_travel_date', models.DateTimeField(null=True)),
                ('Airline', models.CharField(choices=[('Air_India', 'Air India'), ('Indigo', 'Indigo'), ('Spicejet', 'Spicejet'), ('Go_Air', 'Go Air'), ('Vistara', 'Vistara')], default='none', max_length=100)),
                ('Travel_type', models.CharField(choices=[('first_class', 'First Class'), ('economy_class', 'Economy Class'), ('business_class', 'Business Class')], default='none', max_length=100)),
                ('No_of_passeengers', models.IntegerField(default=0)),
                ('Price', models.IntegerField(null=True)),
                ('International_trip', models.BooleanField(default=False)),
            ],
        ),
    ]