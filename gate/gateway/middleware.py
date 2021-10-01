from __future__ import unicode_literals
import logging
import sys
import traceback
from django.utils.deprecation import MiddlewareMixin
from datetime import datetime

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def setup_logger(logger_name, log_file, level=logging.INFO):
    l = logging.getLogger(logger_name)
    formatter = logging.Formatter('%(message)s')
    fileHandler = logging.FileHandler(log_file)
    fileHandler.setFormatter(formatter)

    l.setLevel(level)
    l.addHandler(fileHandler)

setup_logger('gateway_requests', 'logs/gateway_requests.log')
setup_logger('gateway_error_logs', 'logs/gateway.log')
setup_logger('gateway_error_logs_concise', 'logs/gateway_concise.log')


class GatewayLoggingMiddleware(MiddlewareMixin):

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        dir(request)
        now = datetime.now()
        ip = get_client_ip(request)

        logger1 = logging.getLogger('gateway_requests')
        _, _, stacktrace = sys.exc_info()
        logger1.error(
            """%s --  IP ADDRESS: %s, Processing at %s """,now,ip,
            request.path)
        return self.get_response(request)

    def process_exception(self, request, exception):
        ip = get_client_ip(request)
        now = datetime.now()
        logger1= logging.getLogger('gateway_error_logs')
        logger2 = logging.getLogger('gateway_error_logs_concise')
        _, _, stacktrace = sys.exc_info()
        logger1.error(
            """%s -- Processing exception %s at %s.
            GET %s , IP ADDRESS: %s,
            Traceback %s """,now,
            exception, request.path, request.GET,ip,
            ''.join(traceback.format_tb(stacktrace)))


        logger2.error(
            """ -- %s  %s at %s  """,
           now, exception, request.path)
        return None

