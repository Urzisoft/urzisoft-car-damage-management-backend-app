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
        serializer = CarsReportSerializer(data_objects, many=True)

        print(car_damage_severity_detector(settings.MEDIA_ROOT.replace('/MEDIA/', '') + serializer.data[0]['image_url']))

        return Response(serializer.data)

    @staticmethod
    def post(request):
        serializer = CarsReportSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(data=serializer.data, status=status.HTTP_201_CREATED)

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

