from django.shortcuts import render
from rest_framework import viewsets
from .models import Shop
from .serializers import ShopSerializer

class ShopViewSet(viewsets.ModelViewSet):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer


from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import LocationSerializer

@api_view(['GET'])
def get_nearby_shops(request):
    location_serializer = LocationSerializer(data=request.query_params)
    location_serializer.is_valid(raise_exception=True)
    latitude = location_serializer.validated_data['latitude']
    longitude = location_serializer.validated_data['longitude']
    distance = location_serializer.validated_data['distance']
    nearby_shops = Shop.objects.filter(latitude__range=(latitude - 0.01, latitude + 0.01),
                                       longitude__range=(longitude - 0.01, longitude + 0.01))
    serializer = ShopSerializer(nearby_shops, many=True)
    return Response(serializer.data)