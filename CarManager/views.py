from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from knox.models import AuthToken
from rest_framework.generics import GenericAPIView
from knox.auth import TokenAuthentication

from CarDamageManagement import settings
from Classifier.car_damage_severity_detector import car_damage_severity_detector
from CarManager.models import CarsReport
from CarManager.serializer import CarsReportSerializer, LoginUserSerializer, UserSerializer


class CarsReportRestInterface(APIView):
    authentication_classes = [BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    @staticmethod
    def get(request):
        damage_dispatcher = request.GET.get('damage_severity')
        service_done_dispatcher = request.GET.get('is_car_service_done')
        field_to_order_by = request.GET.get('field_to_order_by')
        element_to_order_by = request.GET.get('element_to_order_by')

        if damage_dispatcher:
            data_objects = CarsReport.objects.filter(damage_severity=damage_dispatcher)
        elif service_done_dispatcher:
            data_objects = CarsReport.objects.filter(done=service_done_dispatcher)
        elif field_to_order_by and element_to_order_by:
            field_type = '-' + field_to_order_by if element_to_order_by == 'newest' else field_to_order_by
            data_objects = CarsReport.objects.order_by(field_type)
        else:
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
