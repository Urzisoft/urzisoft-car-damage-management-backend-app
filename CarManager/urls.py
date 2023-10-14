from django.urls import path
from knox import views as knox_views
from . import views


urlpatterns = [
    path('cars/', views.CarsReportRestInterface.as_view(), name='CarsReportRestInterface'),
    path('login-account/', views.LoginAPI.as_view(), name='LoginAccount'),
    path('logout/', knox_views.LogoutView.as_view(), name='knox_logout')
]
