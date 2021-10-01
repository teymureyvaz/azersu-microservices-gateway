from __future__ import unicode_literals
import logging
import sys
import traceback
from django.utils import timezone
def setup_logger(logger_name, log_file, level=logging.INFO):
    l = logging.getLogger(logger_name)
    formatter = logging.Formatter('%(message)s')
    fileHandler = logging.FileHandler(log_file, mode='w')
    fileHandler.setFormatter(formatter)

    l.setLevel(level)
    l.addHandler(fileHandler)

class LdapLoggingMiddleware(object):

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        return self.get_response(request)

    def process_exception(self, request, exception):
        now = timezone.now()
        setup_logger('structure', 'logs/structure.log')
        setup_logger('structure_concise', 'logs/structure_concise.log')
        logger1= logging.getLogger('structure')
        logger2 = logging.getLogger('structure_concise')
        _, _, stacktrace = sys.exc_info()
        logger1.error(
            """%s, Processing exception %s at %s.
            GET %s
            Traceback %s """,
            now,
            exception, request.path, request.GET,
            ''.join(traceback.format_tb(stacktrace)))

        logger2.error(
            """-- %s  %s at %s  """,
            now, exception, request.path)
        return None

