from rest_framework import serializers
from .models import *


class CarsReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarsReport
        fields = '__all__'
