from rest_framework.decorators import api_view
from rest_framework.response import Response
# from django.shortcuts import render
from .models import Restaurant
from .serializer import RestaurantSerializer


@api_view (['GET','POST','PUT','DELETE'])

def showRestaurants(request, restaurant_id= None):
    if request.method =='GET':
        if restaurant_id is not None:
            restaurant = Restaurant.objects.filter(id=restaurant_id).first()
            if Restaurant is not None:
                serializer = RestaurantSerializer(Restaurant)
                return Response(serializer.data)
            return Response({'error':'Restaurant not found'})
        else:
            restaurants = Restaurant.objects.all()
            serializer = RestaurantSerializer(restaurants, many=True)
            return Response(serializer.data)
    elif request.method =='POST':
        serializer = RestaurantSerializer(data=request.data)
        if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=201)
        return Response (serializer.errors, status = 400)   
    elif request.method == 'PUT':
        restaurant = Restaurant.objects.filter(id= restaurant.id).first()
        if restaurant is not None:
            serializer = RestaurantSerializer(restaurant, data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.error,status=400)
        return Response({'error':'Restaurant not found'}, status = 404)
    elif request.method == 'DELETE':
        restaurant = Restaurant.objects.filter(id= restaurant_id).first()
        if restaurant is not None:
            restaurant.delete()
            return Response(status= 204)
        return Response({'error':'Restaurant not found'}, status = 404)
    return Response(status = 400)

    
        
        
        

# Create your views here.
