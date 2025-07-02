from rest_framework import generics
from .models import Car
from .serializers import CarSerializer

class CarListView(generics.ListAPIView):
    serializer_class = CarSerializer

    def get_queryset(self):
        queryset = Car.objects.filter(is_available=True)
        car_class = self.request.query_params.get('class')
        if car_class:
            queryset = queryset.filter(car_class=car_class)
        return queryset
