from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from knox.models import AuthToken
from rest_framework.generics import GenericAPIView

from CarDamageManagement import settings
from Classifier.car_damage_severity_detector import car_damage_severity_detector
from CarManager.models import CarsReport
from CarManager.serializer import CarsReportSerializer, LoginUserSerializer, UserSerializer


class CarsReportRestInterface(APIView):
    permission_classes = [permissions.IsAuthenticated, ]

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


class LoginAPI(GenericAPIView):
    serializer_class = LoginUserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
        })
