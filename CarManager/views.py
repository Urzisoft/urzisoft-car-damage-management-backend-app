from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from CarManager.models import CarsReport
from CarManager.serializer import CarsReportSerializer


class CarsReportRestInterface(APIView):
    @staticmethod
    def get(request):
        data_objects = CarsReport.objects.all()
        serializer = CarsReportSerializer(data_objects, many=True)

        return Response(serializer.data)

    @staticmethod
    def post(request):
        serializer = CarsReportSerializer(data=request.data, many=True)

        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

