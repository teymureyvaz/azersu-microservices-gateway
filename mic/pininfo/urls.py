from django.urls import path, include
from . import views

urlpatterns = [
    path('pin/', views.GetInfoByPin.as_view(), name='pin_info'),
]