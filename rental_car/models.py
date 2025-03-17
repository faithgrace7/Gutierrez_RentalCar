from django.db import models
from django.contrib.auth.models import User

# Extend User model to add extra fields
class UserProfile(models.Model):
    account = models.OneToOneField(User, on_delete=models.CASCADE)
    contact_number = models.CharField(max_length=15, blank=True, null=True)
    home_address = models.TextField(blank=True, null=True)
    reward_points = models.IntegerField(default=0)

    def __str__(self):
        return self.account.username

class Car(models.Model):
    CAR_TYPES = [
        ('Sedan', 'Sedan'),
        ('SUV', 'SUV'),
        ('Luxury', 'Luxury'),
    ]

    model_name = models.CharField(max_length=100)
    category = models.CharField(max_length=50, choices=CAR_TYPES)
    rental_rate = models.DecimalField(max_digits=10, decimal_places=2)
    fuel_category = models.CharField(max_length=50)
    gearbox = models.CharField(max_length=50)
    extra_features = models.TextField(blank=True, null=True)  # GPS, Child seat, etc.
    rental_location = models.CharField(max_length=100, default="Main Branch")  # City of the car
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.model_name
    



class Transaction(models.Model):
    related_reservation = models.ForeignKey('rental_car.Reservation', 
    on_delete=models.CASCADE)
    date = models.DateField()


class Feedback(models.Model):
    reviewer = models.ForeignKey(User, on_delete=models.CASCADE)
    reviewed_car = models.ForeignKey(Car, on_delete=models.CASCADE)
    score = models.IntegerField()
    review_text = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.reviewer.username} - {self.reviewed_car.model_name}"

class Alert(models.Model):
    recipient = models.ForeignKey(User, on_delete=models.CASCADE)
    notification_text = models.TextField()
    timestamp_sent = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Alert for {self.recipient.username}"

class RewardsProgram(models.Model):
    participant = models.ForeignKey(User, on_delete=models.CASCADE)
    earned_points = models.IntegerField(default=0)
    last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.participant.username} - {self.earned_points} Points"

from django.db import models
from django.db.models import Avg
from django.contrib.auth.models import User

class Reservation(models.Model):
    PAYMENT_STATE = [
        ('Pending', 'Pending'),
        ('Successful', 'Successful'),
        ('Failed', 'Failed'),
    ]
    
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    total_cost = models.DecimalField(max_digits=10, decimal_places=2)
    payment_state = models.CharField(max_length=20, choices=PAYMENT_STATE, default='Pending')

    def __str__(self):
        return f"{self.customer.username} - {self.payment_state}"

    @classmethod
    def get_average_sales(cls):
        return cls.objects.filter(payment_state="Successful").aggregate(avg_sales=Avg("total_cost"))["avg_sales"]
