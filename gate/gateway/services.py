import requests
from django.http.response import JsonResponse
from rest_framework.exceptions import APIException, NotFound
from .base_url_address import base_url



class LDAP:

    def get_url(self, function_name):
        module_url='ldap/'
        url_lib = {
            'login': [base_url + module_url + 'login/', 'POST'],
            'logout': [base_url + module_url + 'logout/', 'POST'],
            'check': [base_url + module_url + 'check_token/', 'POST'],
        }
        url = url_lib.get(function_name, [base_url + module_url, 'POST'])

        return url

    def call_api(self,function_name, data):

        url = self.get_url(function_name)
        try:
            r = requests.post(url[0], json=data) if url[1] == 'POST' else requests.get(url[0])
        except requests.exceptions.Timeout as e:
            raise APIException("Connection timed out")
        except requests.exceptions.HTTPError as e:
            raise APIException("HTTP error occured")
        except requests.exceptions.ConnectionError as e:
            raise APIException("ConnectionError")
        except requests.exceptions.URLRequired as e:
            raise APIException("A valid URL is required to make a request")
        except requests.exceptions.TooManyRedirects as e:
            raise APIException("Too many redirects")
        except Exception as e:
            raise APIException("There was a problem")


        try:
            r.raise_for_status()
        except requests.exceptions.HTTPError as e:
            if r.status_code == 404:
                raise NotFound('not found error ' + str(e))
            elif r.status_code == 500:
                raise APIException("Internal server error")
            elif r.status_code == 400:
                raise APIException("Bad request")
            elif r.status_code == 405:
                raise APIException("Method Not Allowed")
            elif r.status_code == 403:
                raise APIException("Forbidden")
            elif r.status_code == 410:
                raise APIException("Gone,not found")
            else:
                raise APIException(str(e))
        else:
            return JsonResponse(r.json(), safe=False)


class MHM:

    def get_url(self, function_name):

        module_url='pininfo/'
        url_lib = {
            'pinInfo': [base_url + module_url + 'pin/', 'POST'],
        }
        url = url_lib.get(function_name, [base_url + module_url, 'POST'])

        return url

    def call_api(self, function_name, data):

        url = self.get_url(function_name)
        try:
            r = requests.post(url[0], json=data) if url[1] == 'POST' else requests.get(url[0])
        except requests.exceptions.Timeout as e:
            raise APIException("Connection timed out")
        except requests.exceptions.HTTPError as e:
            raise APIException("HTTP error occured")
        except requests.exceptions.ConnectionError as e:
            raise APIException("ConnectionError")
        except requests.exceptions.URLRequired as e:
            raise APIException("A valid URL is required to make a request")
        except requests.exceptions.TooManyRedirects as e:
            raise APIException("Too many redirects")

        except Exception as e:
            raise APIException("There was a problem")


        try:
            r.raise_for_status()
            print(r)
        except requests.exceptions.HTTPError as e:
            #print(r.status_code)
            if r.status_code == 404:
                raise NotFound('Not found error ' + str(e))
            elif r.status_code == 500:
                raise APIException("Internal server error")
            elif r.status_code == 400:
                raise APIException("Bad request")
            elif r.status_code == 405:
                raise APIException("Method Not Allowed")
            elif r.status_code == 403:
                raise APIException("Forbidden")
            elif r.status_code == 410:
                raise APIException("Gone,not found")
            else:
                raise APIException(str(e))
        else:
            return JsonResponse(r.json(), safe=False)


class Struktur:

    def get_url(self, function_name, oth_id=''):

        module_url = 'structure/'
        url_lib = {
            'employees_all': [base_url + module_url + 'employees/', 'GET'],
            'employees_detail': [base_url + module_url + 'employees/' + oth_id, 'GET'],
            'departments_all': [base_url + module_url + 'departments/', 'GET'],
            'departments_detail': [base_url + module_url + 'departments/' + oth_id, 'GET'],
            'organizations_all': [base_url + module_url + 'organizations/', 'GET'],
            'organizations_detail': [base_url + module_url + 'organizations/' + oth_id, 'GET'],
            'positions_all': [base_url + module_url + 'positions/', 'GET'],
            'positions_detail': [base_url + module_url + 'positions/' + oth_id, 'GET'],
            'structure_all': [base_url + module_url + 'structure/', 'GET'],
            'structure_detail': [base_url + module_url + 'structure/' + oth_id, 'GET'],
        }
        url = url_lib.get(function_name, [base_url + module_url, 'POST'])
        print(url)
        return url

    def call_api(self, function_name, data=None, oth_id=''):
        url = self.get_url(function_name, oth_id)
        try:
            r = requests.post(url[0], json=data) if url[1] == 'POST' else requests.get(url[0])
        except requests.exceptions.Timeout as e:
            raise APIException("Connection timed out")
        except requests.exceptions.HTTPError as e:
            raise APIException("HTTP error occured")
        except requests.exceptions.ConnectionError as e:
            raise APIException("ConnectionError")
        except requests.exceptions.URLRequired as e:
            raise APIException("A valid URL is required to make a request")
        except requests.exceptions.TooManyRedirects as e:
            raise APIException("Too many redirects")
        except Exception as e:
            raise APIException("There was a problem")

        try:
            r.raise_for_status()
        except requests.exceptions.HTTPError as e:
            if r.status_code == 404:
                raise NotFound('Not found error ' + str(e))
            elif r.status_code == 500:
                raise APIException("Internal server error")
            #elif əlavə edildi
            elif r.status_code == 400:
                raise APIException("Bad request")
            elif r.status_code == 405:
                raise APIException("Method Not Allowed")
            elif r.status_code == 403:
                raise APIException("Forbidden")
            elif r.status_code == 410:
                raise APIException("Gone,not found")
            else:
                raise APIException(str(e))
        else:
            return JsonResponse(r.json(), safe=False)


class SubscriberInfo:

    def get_url(self, function_name,month):

        module_url='consumption_info/'
        url_lib = {
            'subscriber_details': [base_url + module_url + 'subscriber_details/', 'POST'],
            'subscriber_sales': [base_url + module_url + 'subscriber_sales/' + str(month), 'POST'],
            'name_changes': [base_url + module_url + 'ad_deyisiklik/', 'POST'],
            'counter_info': [base_url + module_url + 'counter_info/', 'POST']
        }
        url = url_lib.get(function_name, [base_url + module_url, 'POST'])

        return url

    def call_api(self,function_name, data,month=None):
        url = self.get_url(function_name,month)
        try:
            r = requests.post(url[0], json=data) if url[1] == 'POST' else requests.get(url[0])
        except requests.exceptions.Timeout as e:
            raise APIException("Connection timed out")
        except requests.exceptions.HTTPError as e:
            raise APIException("HTTP error occured")
        except requests.exceptions.ConnectionError as e:
            raise APIException("ConnectionError")
        except requests.exceptions.URLRequired as e:
            raise APIException("A valid URL is required to make a request")
        except requests.exceptions.TooManyRedirects as e:
            raise APIException("Too many redirects")
        except Exception as e:
            raise APIException("There was a problem")


        try:
            r.raise_for_status()
        except requests.exceptions.HTTPError as e:
            if r.status_code == 404:
                raise NotFound('not found error ' + str(e))
            elif r.status_code == 500:
                raise APIException("Internal server error")
            elif r.status_code == 400:
                raise APIException("Bad request")
            elif r.status_code == 405:
                raise APIException("Method Not Allowed")
            elif r.status_code == 403:
                raise APIException("Forbidden")
            elif r.status_code == 410:
                raise APIException("Gone,not found")
            else:
                raise APIException(str(e))
        else:
            return JsonResponse(r.json(), safe=False)

