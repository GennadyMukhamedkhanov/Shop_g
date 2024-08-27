from django.http import HttpResponse
import logging

class Testing1Middleware:
    def __init__(self, get_response):
        self._get_response = get_response

    def __call__(self, request):

        logging.basicConfig(level=logging.INFO, filename="py_log.log", filemode="w", format="%(asctime)s %(levelname)s %(message)s")

        logging.info(f'request method {request.method}')
        logging.info(f'request path_info {request.path_info}')

        response = self._get_response(request)

        logging.info(f'response status_code {response.status_code}')

        return response

    def process_exception(self, request, exception):
        logging.error(exception)

        return HttpResponse(f'Ошибка следующая ---- {exception}')
