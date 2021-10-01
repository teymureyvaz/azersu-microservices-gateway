from django.urls import path, include
from . import views

urlpatterns = [
    path('subscriber_details/', views.SubscriberView.as_view(), name='subscriber_details'),
    path('subscriber_sales/<int:month>', views.SubscriberSalesView.as_view(), name='subscriber_sales'),
    path('ad_deyisiklik/', views.AdDeyisiklik.as_view(), name='ad_deyisiklik'),
    path('counter_info/', views.CounterInfoView.as_view(), name='counter_info')
]