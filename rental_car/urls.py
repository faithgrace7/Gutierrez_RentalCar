from django.urls import path
from .views import CarListCreateAPIView, CarRetrieveUpdateDestroyAPIView


urlpatterns = [
    path('rental_car/', CarListCreateAPIView.as_view(), name='rental_car-list-create'),
    path('rental_car/<int:pk>/', CarRetrieveUpdateDestroyAPIView.as_view(), name='rental_car-retrieve-update-destroy')
]