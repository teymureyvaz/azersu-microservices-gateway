from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    # Services for LDAP
    path('api/v1/ldap/login/', views.LoginToLdap.as_view(), name='Login'),
    path('api/v1/ldap/logout/', views.LogoutFromLdap.as_view(), name='Logout'),
    path('api/v1/ldap/check/', views.CheckTokenValidity.as_view(), name='Check'),

    # Services for get PIN info
    path('api/v1/pin/info/', views.GetPinInfo.as_view(), name='pin_info'),

    # Services for obtain token for login
    path('api/v1/token-auth/', obtain_auth_token, name='api_token_auth'),

    # Services for Azersu Structure
    path('api/v1/structure/employees/', views.EmployeesView.as_view(), name='employee'),
    path('api/v1/structure/employees/<str:employee_id>', views.EmployeeDetailView.as_view(), name='employee_detail'),
    path('api/v1/structure/departments/', views.DepartmentView.as_view(), name='departments'),
    path('api/v1/structure/departments/<str:department_id>', views.DepartmentDetailView.as_view(), name='department_detail'),
    path('api/v1/structure/organisations/', views.OrganisationView.as_view(), name='organisation_all'),
    path('api/v1/structure/organisations/<str:organisation_id>', views.OrganisationDetailView.as_view(), name='organisation_detail'),
    path('api/v1/structure/positions/', views.PositionView.as_view(), name='position_all'),
    path('api/v1/structure/positions/<str:position_id>', views.PositionDetailView.as_view(), name='position_detail'),
    path('api/v1/structure/structure/', views.StructureView.as_view(), name='structure_all'),
    path('api/v1/structure/structure/<str:structure_id>', views.StructureDetailView.as_view(), name='structure_detail'),

    #Services for consumption info
    path('api/v1/consumption_info/subscriber_detail/', views.SubscriberInfoView.as_view(), name='subscriber_detail'),
    path('api/v1/consumption_info/subscriber_sales/', views.SubscriberSalesView.as_view(), name='subscriber_sales'),
    path('api/v1/consumption_info/name_changes/', views.NameChangesView.as_view(), name='name_changes'),
    path('api/v1/consumption_info/counter_info/', views.CounterInfoView.as_view(), name='counter_info'),
]