from django.urls import path, include
from . import views

urlpatterns = [
    path('login/', views.login_with_ldap.as_view(), name='login'),
    path('logout/', views.logout_from_ldap.as_view(), name='logout'),
    path('check_token/', views.check_token_validity.as_view(), name='logout')
]