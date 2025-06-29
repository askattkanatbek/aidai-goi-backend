from rest_framework.generics import ListAPIView
from .models import Car
from .serializers import CarSerializer

class AvailableCarsView(ListAPIView):
    serializer_class = CarSerializer

    def get_queryset(self):
        queryset = Car.objects.all()
        car_class = self.request.query_params.get('class')
        if car_class:
            queryset = queryset.filter(car_class=car_class)
        return queryset
