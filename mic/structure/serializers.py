from rest_framework import serializers


class EmployeesSerializer(serializers.Serializer):
    contract_date = serializers.DateTimeField()
    department_name_id = serializers.CharField(max_length=32)
    employee_id = serializers.CharField(max_length=64)
    patronymic_name = serializers.CharField(max_length=64)
    first_name = serializers.CharField(max_length=64)
    last_name = serializers.CharField(max_length=64)
    org_unit_id = serializers.CharField(max_length=64)
    position_id = serializers.CharField(max_length=64)
    resign_date = serializers.DateTimeField()
    fin_code = serializers.CharField(max_length=32)
    rank = serializers.CharField(max_length=32)

class EmployeesParentSerializer(serializers.Serializer):
	employees = EmployeesSerializer(many=True)

class EmployeeSerializer(serializers.Serializer):
    contract_date = serializers.DateTimeField()
    department_name_id = serializers.CharField(max_length=32)
    employee_id = serializers.CharField(max_length=64)
    patronymic_name = serializers.CharField(max_length=64)
    first_name = serializers.CharField(max_length=64)
    last_name = serializers.CharField(max_length=64)
    org_unit_id = serializers.CharField(max_length=64)
    position_id = serializers.CharField(max_length=64)
    resign_date = serializers.DateTimeField()
    status = serializers.CharField(max_length=16)
    fin_code = serializers.CharField(max_length=32)
    rank = serializers.CharField(max_length=32)


class DepartmentNamesSerializer(serializers.Serializer):
    department_name_id = serializers.CharField(max_length=32)
    department_name = serializers.CharField(max_length=500)

class DepartmentNamesParentSerializer(serializers.Serializer):
	department_info = DepartmentNamesSerializer(many=True, source='department_names')

class DepartmentNameSerializer(serializers.Serializer):
    department_name_id = serializers.CharField(max_length=32)
    department_name = serializers.CharField(max_length=500)


class OrganisationNamesSerializer(serializers.Serializer):
    org_name_id = serializers.IntegerField()
    org_name = serializers.CharField(max_length=500)

class OrganisationNamesParentSerializer(serializers.Serializer):
	organizations = OrganisationNamesSerializer(many=True)

class OrganisationNameSerializer(serializers.Serializer):
    org_name_id = serializers.IntegerField()
    org_name = serializers.CharField(max_length=500)


class PositionNamesSerializer(serializers.Serializer):
    position_id = serializers.CharField(max_length=64)
    position_name = serializers.CharField(max_length=500)

class PositionNamesParentSerializer(serializers.Serializer):
	positions = PositionNamesSerializer(many=True)

class PositionNameSerializer(serializers.Serializer):
    position_id = serializers.CharField(max_length=64)
    position_name = serializers.CharField(max_length=500)


class DepartmentStructuresSerializer(serializers.Serializer):
    org_name_id = serializers.IntegerField()
    parent_department_name_id = serializers.CharField(max_length=64)
    department_name_id = serializers.CharField(max_length=64)

class DepartmentStructuresParentSerializer(serializers.Serializer):
	department_structure = DepartmentStructuresSerializer(many=True)

class DepartmentStructureSerializer(serializers.Serializer):
    org_name_id = serializers.IntegerField()
    parent_department_name_id = serializers.CharField(max_length=64)
    department_name_id = serializers.CharField(max_length=64)
    status = serializers.CharField(max_length=16)