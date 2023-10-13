from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from CarDamageManagement import settings
from Classifier.car_damage_severity_detector import car_damage_severity_detector
from CarManager.models import CarsReport
from CarManager.serializer import CarsReportSerializer


class CarsReportRestInterface(APIView):
    @staticmethod
    def get(request):
        data_objects = CarsReport.objects.all()
        serializers = CarsReportSerializer(data_objects, many=True)

        return Response(serializers.data)

    @staticmethod
    def post(request):
        serializer = CarsReportSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            serializer.validated_data['damage_severity'] = \
                car_damage_severity_detector(settings.MEDIA_ROOT + 'car-manager/data-to-identify/'
                                             + str(serializer.validated_data['image_url']))

            serializer.save()

            return Response(data=serializer.data, status=status.HTTP_201_CREATED)

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

