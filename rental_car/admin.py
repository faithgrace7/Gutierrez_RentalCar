from django.contrib import admin
from .models import Car, Reservation, UserProfile, Transaction, Feedback, Alert, RewardsProgram

admin.site.register(Car)
admin.site.register(Reservation)
admin.site.register(UserProfile)
admin.site.register(Transaction)
admin.site.register(Feedback)
admin.site.register(Alert)
admin.site.register(RewardsProgram)
