from django.urls import path
from .views import AvailableCarsView

urlpatterns = [
    path('cars/', AvailableCarsView.as_view(), name='available-cars'),
]
