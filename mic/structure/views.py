from rest_framework.response import Response
from rest_framework import status
from rest_framework import views
import json
from . import serializers
import os
import cx_Oracle

# Create your views here.

os.environ["NLS_LANG"] = "AZERBAIJANI.UTF8"

class EmployeesView(views.APIView):

	def get(self, request):
		serializer = serializers.EmployeesParentSerializer(instance=self.get_context_data(request))
		return Response(serializer.data)

	def post(self):
		content = {'content': 'Method Not Allowed'}
		return Response(content, status=status.HTTP_405_METHOD_NOT_ALLOWED)

	def get_context_data(self, request):
		con = cx_Oracle.connect('msalimov/Muhammed123@192.168.9.105:1521/MISDB')
		cur = con.cursor()
		cur.execute('select * from ERP.erp_1c_employees where status=\'A\'')
		employees = list()
		try:
			res = cur.fetchall()
			for i in res:
				employee_data = {
					'contract_date': i[1],
					'department_name_id': i[2],
					'employee_id': i[4],
					'patronymic_name': i[5],
					'first_name': i[6],
					'last_name': i[7],
					'org_unit_id': i[8],
					'position_id': i[10],
					'resign_date': i[11],
					'fin_code': i[16],
					'rank': i[17],
				}
				employees.append(employee_data)
		except:
			employee_data = {
				'contract_date': '',
				'department_name_id': '',
				'employee_id': '',
				'patronymic_name': '',
				'first_name': '',
				'last_name': '',
				'org_unit_id': '',
				'position_id': '',
				'resign_date': '',
				'fin_code': '',
				'rank': '',
			}
			employees.append(employee_data)
		return {'employees': employees}

class EmployeeView(views.APIView):

	def get(self, request, employee_id):
		serializer = serializers.EmployeeSerializer(instance=self.get_context_data(request, employee_id=employee_id))
		return Response(serializer.data)

	def post(self):
		content = {'content': 'Method Not Allowed'}
		return Response(content, status=status.HTTP_405_METHOD_NOT_ALLOWED)

	def get_context_data(self, request, employee_id):
		con = cx_Oracle.connect('msalimov/Muhammed123@192.168.9.105:1521/MISDB')
		cur = con.cursor()
		query = 'select * from ERP.erp_1c_employees where employee_id=\'{}\''.format(employee_id)
		cur.execute(query)
		try:
			res = cur.fetchall()[0]
			employee_data = {
				'contract_date': res[1],
				'department_name_id': res[2],
				'employee_id': res[4],
				'patronymic_name': res[5],
				'first_name': res[6],
				'last_name': res[7],
				'org_unit_id': res[8],
				'position_id': res[10],
				'resign_date': res[11],
				'status': res[14],
				'fin_code': res[16],
				'rank': res[17],
			}
		except:
			employee_data = {
				'contract_date': '',
				'department_name_id': '',
				'employee_id': '',
				'patronymic_name': '',
				'first_name': '',
				'last_name': '',
				'org_unit_id': '',
				'position_id': '',
				'resign_date': '',
				'status': '',
				'fin_code': '',
				'rank': '',
			}

		return employee_data

class DepartmentNamesView(views.APIView):

	def get(self, request):
		serializer = serializers.DepartmentNamesParentSerializer(instance=self.get_context_data(request))
		return Response(serializer.data)

	def post(self):
		content = {'content': 'Method Not Allowed'}
		return Response(content, status=status.HTTP_405_METHOD_NOT_ALLOWED)

	def get_context_data(self, request):
		con = cx_Oracle.connect('msalimov/Muhammed123@192.168.9.105:1521/MISDB')
		cur = con.cursor()
		cur.execute('select * from ERP.erp_1c_department_names where status=\'A\'')
		res = cur.fetchall()
		departments = list()
		for i in res:
			department_data = {
				'department_name_id': i[0],
				'department_name': i[1],
			}
			departments.append(department_data)

		return {'department_names': departments}

class DepartmentNameView(views.APIView):

	def get(self, request, department_id):
		serializer = serializers.DepartmentNameSerializer(instance=self.get_context_data(request, department_id=department_id))
		return Response(serializer.data)

	def post(self):
		content = {'content': 'Method Not Allowed'}
		return Response(content, status=status.HTTP_405_METHOD_NOT_ALLOWED)

	def get_context_data(self, request, department_id):
		con = cx_Oracle.connect('msalimov/Muhammed123@192.168.9.105:1521/MISDB')
		cur = con.cursor()
		query = 'select * from ERP.erp_1c_department_names where department_name_id=\'{}\''.format(department_id)
		#print(query)
		cur.execute(query)
		try:
			res = cur.fetchall()[0]
			department_data = {
				'department_name_id': res[0],
				'department_name': res[1],
			}
		except:
			department_data = {
				'department_name_id': '',
				'department_name': '',
			}

		return department_data


class OrganisationNamesView(views.APIView):

	def get(self, request):
		serializer = serializers.OrganisationNamesParentSerializer(instance=self.get_context_data(request))
		return Response(serializer.data)

	def post(self):
		content = {'content': 'Method Not Allowed'}
		return Response(content, status=status.HTTP_405_METHOD_NOT_ALLOWED)

	def get_context_data(self, request):
		con = cx_Oracle.connect('msalimov/Muhammed123@192.168.9.105:1521/MISDB')
		cur = con.cursor()
		cur.execute('select * from ERP.erp_1c_organization_names')
		res = cur.fetchall()
		organizations = list()
		for i in res:
			organization_data = {
				'org_name_id': i[0],
				'org_name': i[1],
			}
			organizations.append(organization_data)

		return {'organizations': organizations}

class OrganisationNameView(views.APIView):

	def get(self, request, organisation_id):
		serializer = serializers.OrganisationNameSerializer(instance=self.get_context_data(request, organisation_id=organisation_id))
		return Response(serializer.data)

	def post(self):
		content = {'content': 'Method Not Allowed'}
		return Response(content, status=status.HTTP_405_METHOD_NOT_ALLOWED)

	def get_context_data(self, request, organisation_id):
		con = cx_Oracle.connect('msalimov/Muhammed123@192.168.9.105:1521/MISDB')
		cur = con.cursor()
		query = 'select * from ERP.erp_1c_organization_names where org_name_id=\'{}\''.format(organisation_id)
		#print(query)
		cur.execute(query)
		try:
			res = cur.fetchall()[0]
			organization_data = {
				'org_name_id': res[0],
				'org_name': res[1],
			}
		except:
			organization_data = {
				'org_name_id': '',
				'org_name': '',
			}
		return organization_data

class PositionNamesView(views.APIView):

	def get(self, request):
		serializer = serializers.PositionNamesParentSerializer(instance=self.get_context_data(request))
		return Response(serializer.data)

	def post(self):
		content = {'content': 'Method Not Allowed'}
		return Response(content, status=status.HTTP_405_METHOD_NOT_ALLOWED)

	def get_context_data(self, request):
		con = cx_Oracle.connect('msalimov/Muhammed123@192.168.9.105:1521/MISDB')
		cur = con.cursor()
		cur.execute('select * from ERP.erp_1c_position')
		res = cur.fetchall()
		positions = list()
		for i in res:
			position_data = {
				'position_id': i[0],
				'position_name': i[1],
			}
			positions.append(position_data)

		return {'positions': positions}

class PositionNameView(views.APIView):

	def get(self, request, position_id):
		serializer = serializers.PositionNameSerializer(instance=self.get_context_data(request, position_id=position_id))
		return Response(serializer.data)

	def post(self):
		content = {'content': 'Method Not Allowed'}
		return Response(content, status=status.HTTP_405_METHOD_NOT_ALLOWED)

	def get_context_data(self, request, position_id):
		con = cx_Oracle.connect('msalimov/Muhammed123@192.168.9.105:1521/MISDB')
		cur = con.cursor()
		query = 'select * from ERP.erp_1c_position where position_id=\'{}\''.format(position_id)
		#print(query)
		cur.execute(query)
		try:
			res = cur.fetchall()[0]
			position_data = {
				'position_id': res[0],
				'position_name': res[1],
			}
		except:
			position_data = {
				'position_id': '',
				'position_name': '',
			}
		return position_data


class DepartmentStructuresView(views.APIView):

	def get(self, request):
		serializer = serializers.DepartmentStructuresParentSerializer(instance=self.get_context_data(request))
		return Response(serializer.data)

	def post(self):
		content = {'content': 'Method Not Allowed'}
		return Response(content, status=status.HTTP_405_METHOD_NOT_ALLOWED)

	def get_context_data(self, request):
		con = cx_Oracle.connect('msalimov/Muhammed123@192.168.9.105:1521/MISDB')
		cur = con.cursor()
		cur.execute('select * from ERP.erp_1c_department_structure where status=\'A\'')
		res = cur.fetchall()
		structures = list()
		for i in res:
			structure_data = {
				'org_name_id': i[0],
				'parent_department_name_id': i[1],
				'department_name_id': i[2],
			}
			structures.append(structure_data)

		return {'department_structure': structures}

class DepartmentStructureView(views.APIView):

	def get(self, request, structure_id):
		serializer = serializers.DepartmentStructureSerializer(instance=self.get_context_data(request, structure_id=structure_id))
		return Response(serializer.data)

	def post(self):
		content = {'content': 'Method Not Allowed'}
		return Response(content, status=status.HTTP_405_METHOD_NOT_ALLOWED)

	def get_context_data(self, request, structure_id):
		con = cx_Oracle.connect('msalimov/Muhammed123@192.168.9.105:1521/MISDB')
		cur = con.cursor()
		query = 'select * from ERP.erp_1c_department_structure where department_name_id=\'{}\''.format(structure_id)
		#print(query)
		cur.execute(query)
		try:
			res = cur.fetchall()[0]
			structure_data = {
				'org_name_id': res[0],
				'parent_department_name_id': res[1],
				'department_name_id': res[2],
				'status': res[3],
			}
		except:
			structure_data = {
				'org_name_id': '',
				'parent_department_name_id': '',
				'department_name_id': '',
				'status': '',
			}
		return structure_data