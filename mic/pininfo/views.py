import zeep
import base64
from rest_framework.response import Response
from rest_framework import status
from rest_framework import views
import json
from . import serializers
# Create your views here.


class GetInfoByPin(views.APIView):

    def get(self, request):
        content = {'content': 'Method Not Allowed'}
        return Response(content, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def post(self, request):
        data = json.loads(request.body)
        if 'PIN' in data:
            serializer = serializers.pinSerializer(instance=self.get_context_data(request))
            return Response(serializer.data)
        else:
            return Response({'Error': 'Enter "PIN" info'}, status=status.HTTP_400_BAD_REQUEST)

    def get_context_data(self, request):
        data = json.loads(request.body)
        pin_wsdl = 'http://172.16.1.26/Integratedservices/IntegratedServices.asmx?WSDL'
        client = zeep.Client(wsdl=pin_wsdl)
        get_user_data = client.service.getPersonalInfoByPin(data['PIN'])
        print(get_user_data)
        name = get_user_data['Name']
        surname = get_user_data['Surname']
        patronymic = get_user_data['Patronymic']
        birth_date = get_user_data['birthDate']
        if get_user_data['Adress'] != None:
            adress = {
                'menzil': get_user_data['Adress']['apartment'],
                'kuce': get_user_data['Adress']['street'],
                'bina': get_user_data['Adress']['building']
            }
        else:
            adress = None
        citizenship = get_user_data['citizenship']
        #issue_date = get_user_data['issueDate']
        status = get_user_data['status']
        gender = get_user_data['gender']
        photo = base64.b64encode(get_user_data['photo']).decode('ascii')
        expire_date = get_user_data['expdate']
        #blood_type = get_user_data['bloodtype']
        #eye_color = get_user_data['eyecolor']
        #height = get_user_data['height']

        return_data = {
            'ad': name,
            'soyad': surname,
            'ata_adi': patronymic,
            'dogum_tarixi': birth_date,
            'adres': adress,
            'vetendasliq': citizenship,
            'status': status,
            'cins': gender,
            'foto': photo,
            'bitme_tarixi': expire_date,
        }

        return return_data