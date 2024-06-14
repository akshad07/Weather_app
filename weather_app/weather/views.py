from rest_framework import generics
from .models import WeatherData
from .serializers import WeatherDataSerializer
from .utils import fetch_weather_data

class WeatherDataListCreate(generics.ListCreateAPIView):
    queryset = WeatherData.objects.all()
    serializer_class = WeatherDataSerializer

    def perform_create(self, serializer):
        url = self.request.data.get('url')
        weather_data = fetch_weather_data(url)
        for data in weather_data:
            WeatherData.objects.create(**data)
