from django.shortcuts import render
from rest_framework import views, viewsets
import json
from .services import LDAP, MHM, Struktur,SubscriberInfo
from rest_framework.response import Response
from . import serializers
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import  CompanyMonthsLimit
# Create your views here.




class LoginToLdap(views.APIView):
    def get(self, request):
        content = {'content': 'Method Not Allowed'}
        return Response(content, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def post(self, request):
        serializer = serializers.LoginSerializer(instance=self.get_context_data(request))
        return Response(serializer.data)

    def get_context_data(self, request):
        data = json.loads(request.body)
        context = json.loads(LDAP().call_api('login', data).content)
        return context

class LogoutFromLdap(views.APIView):
    def get(self, request):
        content = {'content': 'Method Not Allowed'}
        return Response(content, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def post(self, request):
        serializer = serializers.ResponseSerializer(instance=self.get_context_data(request))
        return Response(serializer.data)

    def get_context_data(self, request):
        data = json.loads(request.body)
        context = json.loads(LDAP().call_api('logout', data).content)
        return context

class CheckTokenValidity(views.APIView):
    def get(self, request):
        content = {'content': 'Method Not Allowed'}
        return Response(content, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def post(self, request):
        serializer = serializers.ResponseCheckSerializer(instance=self.get_context_data(request))
        return Response(serializer.data)

    def get_context_data(self, request):
        data = json.loads(request.body)
        context = json.loads(LDAP().call_api('check', data).content)
        return context

class GetPinInfo(views.APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = {'content': 'Method Not Allowed'}
        return Response(content, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def post(self, request):
        if self.request.user.has_perm('pininfo.pininfo'):
            data = json.loads(request.body)
            context = json.loads(MHM().call_api('pinInfo', data).content)
            serializer = serializers.pinSerializer(instance=context)
            return Response(serializer.data)
        else:
            content = {'content': 'Forbidden'}
            return Response(content, status=status.HTTP_403_FORBIDDEN)
        


class EmployeesView(views.APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        if self.request.user.has_perm('1c_struktur.employees'):
            serializer = serializers.EmployeesParentSerializer(instance=self.get_context_data(request))
            return Response(serializer.data)
        else:
            content = {'content': 'Forbidden'}
            return Response(content, status=status.HTTP_403_FORBIDDEN)


    def post(self, request):
        content = {'content': 'Method Not Allowed'}
        return Response(content, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def get_context_data(self, request):
        context = json.loads(Struktur().call_api('employees_all').content)
        return context

class EmployeeDetailView(views.APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, employee_id):
        if self.request.user.has_perm('1c_struktur.employees'):
            serializer = serializers.EmployeeSerializer(instance=self.get_context_data(request, employee_id))
            return Response(serializer.data)
        else:
            content = {'content': 'Forbidden'}
            return Response(content, status=status.HTTP_403_FORBIDDEN)

    def post(self, request):
        content = {'content': 'Method Not Allowed'}
        return Response(content, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def get_context_data(self, request, employee_id):
        context = json.loads(Struktur().call_api('employees_detail', oth_id=employee_id).content)
        return context

class DepartmentView(views.APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        if self.request.user.has_perm('1c_struktur.department'):
            serializer = serializers.DepartmentNamesParentSerializer(instance=self.get_context_data(request))
            return Response(serializer.data)
        else:
            content = {'content': 'Forbidden'}
            return Response(content, status=status.HTTP_403_FORBIDDEN)


    def post(self, request):
        content = {'content': 'Method Not Allowed'}
        return Response(content, status=status.HTTP_405_METHOD_NOT_ALLOWED)


    def get_context_data(self, request):
        context = json.loads(Struktur().call_api('departments_all').content)
        return context

class DepartmentDetailView(views.APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, department_id):
        if self.request.user.has_perm('1c_struktur.department'):
            serializer = serializers.DepartmentNameSerializer(instance=self.get_context_data(request, department_id))
            return Response(serializer.data)
        else:
            content = {'content': 'Forbidden'}
            return Response(content, status=status.HTTP_403_FORBIDDEN)

    def post(self, request):
        content = {'content': 'Method Not Allowed'}
        return Response(content, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def get_context_data(self, request, department_id):
        context = json.loads(Struktur().call_api('departments_detail', oth_id=department_id).content)
        return context

class OrganisationView(views.APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        if self.request.user.has_perm('1c_struktur.organisation'):
            serializer = serializers.OrganisationNamesParentSerializer(instance=self.get_context_data(request))
            return Response(serializer.data)
        else:
            content = {'content': 'Forbidden'}
            return Response(content, status=status.HTTP_403_FORBIDDEN)

    def post(self, request):
        content = {'content': 'Method Not Allowed'}
        return Response(content, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def get_context_data(self, request):
        context = json.loads(Struktur().call_api('organizations_all').content)
        return context

class OrganisationDetailView(views.APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, organisation_id):
        if self.request.user.has_perm('1c_struktur.organisation'):
            serializer = serializers.OrganisationNameSerializer(instance=self.get_context_data(request, organisation_id))
            return Response(serializer.data)
        else:
            content = {'content': 'Forbidden'}
            return Response(content, status=status.HTTP_403_FORBIDDEN)

    def post(self, request):
        content = {'content': 'Method Not Allowed'}
        return Response(content, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def get_context_data(self, request, organisation_id):
        context = json.loads(Struktur().call_api('organizations_detail', oth_id=organisation_id).content)
        return context

class PositionView(views.APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        if self.request.user.has_perm('1c_struktur.position'):
            serializer = serializers.PositionNamesParentSerializer(instance=self.get_context_data(request))
            return Response(serializer.data)
        else:
            content = {'content': 'Forbidden'}
            return Response(content, status=status.HTTP_403_FORBIDDEN)

    def post(self, request):
        content = {'content': 'Method Not Allowed'}
        return Response(content, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def get_context_data(self, request):
        context = json.loads(Struktur().call_api('positions_all').content)
        return context

class PositionDetailView(views.APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, position_id):
        if self.request.user.has_perm('1c_struktur.position'):
            serializer = serializers.PositionNameSerializer(instance=self.get_context_data(request, position_id))
            return Response(serializer.data)
        else:
            content = {'content': 'Forbidden'}
            return Response(content, status=status.HTTP_403_FORBIDDEN)

    def post(self, request):
        content = {'content': 'Method Not Allowed'}
        return Response(content, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def get_context_data(self, request, position_id):
        context = json.loads(Struktur().call_api('positions_detail', oth_id=position_id).content)
        return context


class StructureView(views.APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        if self.request.user.has_perm('1c_struktur.struktur'):
            serializer = serializers.DepartmentStructuresParentSerializer(instance=self.get_context_data(request))
            return Response(serializer.data)
        else:
            content = {'content': 'Forbidden'}
            return Response(content, status=status.HTTP_403_FORBIDDEN)

    def post(self, request):
        content = {'content': 'Method Not Allowed'}
        return Response(content, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def get_context_data(self, request):
        context = json.loads(Struktur().call_api('structure_all').content)
        return context

class StructureDetailView(views.APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, structure_id):
        if self.request.user.has_perm('1c_struktur.struktur'):
            serializer = serializers.DepartmentStructureSerializer(instance=self.get_context_data(request, structure_id))
            return Response(serializer.data)
        else:
            content = {'content': 'Forbidden'}
            return Response(content, status=status.HTTP_403_FORBIDDEN)

    def post(self, request):
        content = {'content': 'Method Not Allowed'}
        return Response(content, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def get_context_data(self, request, structure_id):
        context = json.loads(Struktur().call_api('structure_detail', oth_id=structure_id).content)
        return context


class SubscriberInfoView(views.APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request):
        content = {'content': 'Method Not Allowed'}
        return Response(content, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def post(self, request):
        if self.request.user.has_perm('consumption_info.subscriber_detail'):
            try:
                subscriber_data = json.loads(request.body)
            except:
                content = {'content': 'Bad Request'}
                return Response(content, status=status.HTTP_400_BAD_REQUEST)

            context = json.loads(SubscriberInfo().call_api('subscriber_details',subscriber_data).content)
            if 'status' in context:
                serializer = serializers.ResponseSerializer(instance=context)
            else:
                serializer = serializers.SubscriberSerializer(instance=context)
            return Response(serializer.data)
        else:
            content = {'content': 'Forbidden'}
            return Response(content, status=status.HTTP_403_FORBIDDEN)

class SubscriberSalesView(views.APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request):
        content = {'content': 'Method Not Allowed'}
        return Response(content, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def post(self, request):
        if self.request.user.has_perm('consumption_info.subscriber_sales'):
            try:
                subscriber_data = json.loads(request.body)
            except:
                content = {'content': 'Bad Request'}
                return Response(content, status=status.HTTP_400_BAD_REQUEST)
            try:
                month = CompanyMonthsLimit.objects.get(company=request.user).months
            except:
                month = 0
            context = json.loads(SubscriberInfo().call_api('subscriber_sales',subscriber_data,month).content)
            if 'status' in context:
                serializer = serializers.ResponseSerializer(instance=context)
            else:
                serializer = serializers.SubscriberSalesSerializer(instance=context, many=True)
            return Response(serializer.data)
        else:
            content = {'content': 'Forbidden'}
            return Response(content, status=status.HTTP_403_FORBIDDEN)

class NameChangesView(views.APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request):
        content = {'content': 'Method Not Allowed'}
        return Response(content, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def post(self, request):
        if self.request.user.has_perm('consumption_info.name_changes'):
            try:
                subscriber_data = json.loads(request.body)
            except:
                content = {'content': 'Bad Request'}
                return Response(content, status=status.HTTP_400_BAD_REQUEST)

            context = json.loads(SubscriberInfo().call_api('name_changes',subscriber_data).content)
            print(context)
            if 'status' in context:
                serializer = serializers.ResponseSerializer(instance=context)
            else:
                serializer = serializers.AdDeyismeSerializer(instance=context, many=True)
            return Response(serializer.data)
        else:
            content = {'content': 'Forbidden'}
            return Response(content, status=status.HTTP_403_FORBIDDEN)
class CounterInfoView(views.APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request):
        content = {'content': 'Method Not Allowed'}
        return Response(content, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def post(self, request):
        if self.request.user.has_perm('consumption_info.counter_info'):
            try:
                subscriber_data = json.loads(request.body)
            except:
                content = {'content': 'Bad Request'}
                return Response(content, status=status.HTTP_400_BAD_REQUEST)

            context = json.loads(SubscriberInfo().call_api('counter_info',subscriber_data).content)
            print(context)
            if 'status' in context:
                serializer = serializers.ResponseSerializer(instance=context)
            else:
                serializer = serializers.CounterInfoSerializer(instance=context, many=True)
            return Response(serializer.data)
        else:
            content = {'content': 'Forbidden'}
            return Response(content, status=status.HTTP_403_FORBIDDEN)