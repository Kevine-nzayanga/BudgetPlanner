from django.urls import path
from .views import showRestaurants

urlpatterns = [
     path('restaurants', showRestaurants, name='displayRestaurant'),
     path('restaurant/<int:restaurant_id>/',showRestaurants, name='restaurant_detail_view'),
     path('restaurants/<int:restaurant_id>/delete/', showRestaurants, name='delete_restaurant_view'),
]
