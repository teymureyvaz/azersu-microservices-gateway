from django.shortcuts import render
import ldap
from rest_framework import views
from rest_framework.response import Response
from rest_framework import status
import json
import datetime
import uuid
from .models import AD_token
from . import serializers
import logging

#logger obyekti yaradilir
logger = logging.getLogger('ldap_token')

# Create your views here.


class login_with_ldap(views.APIView):
    def get(self, request):
        content = {'content': 'Method Not Allowed'}
        return Response(content, status=status.HTTP_405_METHOD_NOT_ALLOWED)
    def post(self, request):
        serializer = serializers.LoginSerializer(instance=self.get_context_data(request))
        return Response(serializer.data)

    def get_context_data(self, request):
        user_data = json.loads(request.body)
        username = user_data['username']
        password = user_data['password']
        #AD_token modelindən movcud tarixi keçmiş token çağırılır.
        check_info_from_db_count = AD_token.objects.filter(username=username, is_active=True,
                                                             expired_at__lt=datetime.datetime.now()).count()
        #Tarixi keçmiş token movcud olduqu halda deaktiv edilir.
        if check_info_from_db_count > 0:
            AD_token.objects.filter(username=username, is_active=True,
                                        expired_at__lt=datetime.datetime.now()).update(is_active=False)

        #Ldap əlaqəsi qurulur.
        is_login = False
        con = ldap.initialize('ldap://azersu.lan')
        con.protocol_version = 3
        con.set_option(ldap.OPT_REFERRALS, 0)
        con.simple_bind_s('{}@azersu.lan'.format(username), password)
        try:
            #istifadəçi təstiqlənir
            con.simple_bind_s('{}@azersu.lan'.format(username), password)
            is_login = True
            logger.error("Test!!")
        except ldap.INVALID_CREDENTIALS:
            response = 'Username or password is incorrect!'
            logger.info(ldap.INVALID_CREDENTIALS)
        except:
            response = 'Error occured'

        #hal hazirda istifadəçiyə aid aktiv tokenin olub olmadıqı yoxlanılır.
        if is_login:
            try:
                get_info_from_db_count = AD_token.objects.filter(username=username, is_active=True,
                                                             expired_at__gt=datetime.datetime.now()).count()
            except AD_token.DoesNotExist:
                logger.error("AD_token object does not exist")

            # print(datetime.datetime.now() - get_info_from_db.expired_at)
            # aktiv token olduqu halda həmin token qaytarılır
            if get_info_from_db_count > 0:
                try:
                    get_info_from_db = AD_token.objects.get(username=username, is_active=True)
                except AD_token.DoesNotExist:
                    logger.error("AD_token object does not exist")
                data = {
                    'username': get_info_from_db.username,
                    'token': get_info_from_db.token,
                    'expire_date': get_info_from_db.expired_at,
                    'status': 200,
                    'message': 'already logged in'
                }
            # aktiv token olmadıqı halda yeni token yaradılıb qaytarılır
            else:
                now = datetime.datetime.now()
                tarix = str(now.year) + str(now.month) + str(now.day) + str(now.hour) + str(now.minute) + str(
                    now.second) + str(now.microsecond)
                token = uuid.uuid5(uuid.NAMESPACE_DNS, tarix)
                db_data = AD_token(username=username, token=token, expired_at=datetime.datetime.now() + datetime.timedelta(days=1))
                db_data.save()
                get_info_from_db = AD_token.objects.get(username=username, token=token)
                data = {
                        'username': get_info_from_db.username,
                        'token': get_info_from_db.token,
                        'expire_date': get_info_from_db.expired_at,
                        'status': 200,
                        'message': 'success'
                    }
        else:
            # ldap istifadəçi adı tapmadıqda xəta qaytarılır
            data = {
                'username': '',
                'token': '',
                'expire_date': '',
                'status': 401,
                'message': 'login failed'
            }

        return data


class logout_from_ldap(views.APIView):

    def get(self, request):
        content = {'content': 'Method Not Allowed'}
        return Response(content, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def post(self, request):
        serializer = serializers.ResponseSerializer(instance=self.get_context_data(request))
        return Response(serializer.data)

    def get_context_data(self, request):
        token = json.loads(request.body)['token']
        #vaxtı keçmiş token çağırılır
        find_token_in_db_count = AD_token.objects.filter(token=token, is_active=True, expired_at__gt=datetime.datetime.now()).count()
        # vaxtı keçməmiş token çağırlır
        find_token_in_db_count2 = AD_token.objects.filter(token=token, is_active=True,
                                                          expired_at__lt=datetime.datetime.now()).count()
        #tokenin vaxtı keçməyibsə 200 qaytarılır,token deaktiv edilir.
        if find_token_in_db_count > 0:
            update_token_in_db = AD_token.objects.filter(token=token).update(is_active=False, expired_at=datetime.datetime.now())
            data = {
                'status': 200,
                'message': 'Logged out successfully'
            }
        # tokenin vaxtı artıq keçmişsə 401 qaytarılır,token deaktiv edilir.
        elif find_token_in_db_count2 > 0:
            AD_token.objects.filter(token=token, is_active=True,
                                    expired_at__lt=datetime.datetime.now()).update(is_active=False, expired_at=datetime.datetime.now())
            data = {
                'status': 401,
                'message': 'Token already expired'
            }
        # token tapılmadıqı halda 410 qaytarılır
        else:
            data={
                'status': 410,
                'message': 'Token not found'
            }

        return data

class check_token_validity(views.APIView):
    
    def get(self, request):
        content = {'content': 'Method Not Allowed'}
        return Response(content, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def post(self, request):
        serializer = serializers.ResponseCheckSerializer(instance=self.get_context_data(request))
        return Response(serializer.data)

    def get_context_data(self, request):
        token = json.loads(request.body)['token']
        #Vaxtı keçməmiş token çağırılır
        find_token_in_db_count = AD_token.objects.filter(token=token, is_active=True, expired_at__gt=datetime.datetime.now())
        #print(find_token_in_db_count.username)
        # Token mövcud olduqu halda,token qaytarılır
        if find_token_in_db_count.count() > 0:
            token_in_db = AD_token.objects.get(token=token, is_active=True,
                                                             expired_at__gt=datetime.datetime.now())
            data = {
                'username': token_in_db.username,
                'status': 200,
                'message': 'token is valid'
            }
        # Token mövcud olmadıqı halda,403 kodu qaytarılır.
        else:
            data = {
                'username': '',
                'status': 403,
                'message': 'token is not valid'
            }

        return data
