from django.urls import path
from . import views


urlpatterns = [
    path('cars', views.CarsReportRestInterface.as_view(), name='CarsReportRestInterface'),
]
