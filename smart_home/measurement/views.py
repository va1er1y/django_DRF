# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response

# from smart_home.measurement.models import transmitter, temperature_measure
# from smart_home.measurement.serializers import MeasurementSerializer, SensorDetailSerializer
from smart_home.measurement.models import transmitter, temperature_measure
from smart_home.measurement.serializers import MeasurementSerializer, SensorDetailSerializer

class sensor(ListAPIView):
    queryset = transmitter.objects.all()
    serializer_class = SensorDetailSerializer

    def post(self, request):
        sensor = request.GET.get("sensor")
        descriptions = request.GET.get("description")
        add_sensor = transmitter(name = sensor, description = descriptions)
        add_sensor.save
        # return Response({'status': 'OK'})


class measure(RetrieveAPIView):
    queryset = temperature_measure.objects.all()
    serializer_class = SensorDetailSerializer