from django.urls import path, include
from . import views

urlpatterns = [
    path('employees/', views.EmployeesView.as_view(), name='employees_list'),
    path('employees/<str:employee_id>', views.EmployeeView.as_view(), name='employee_detail'),

    path('departments/', views.DepartmentNamesView.as_view(), name='department_list'),
    path('departments/<str:department_id>', views.DepartmentNameView.as_view(), name='department_detail'),

    path('organizations/', views.OrganisationNamesView.as_view(), name='organizations_list'),
    path('organizations/<int:organisation_id>', views.OrganisationNameView.as_view(), name='organizations_detail'),

    path('positions/', views.PositionNamesView.as_view(), name='positions_list'),
    path('positions/<str:position_id>', views.PositionNameView.as_view(), name='positions_detail'),

    path('structure/', views.DepartmentStructuresView.as_view(), name='structure_list'),
    path('structure/<str:structure_id>', views.DepartmentStructureView.as_view(), name='structure_detail'),
]