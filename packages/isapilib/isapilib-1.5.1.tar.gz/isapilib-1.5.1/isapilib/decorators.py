from django.http import JsonResponse
from rest_framework.request import Request

from isapilib.exceptions import SepaException
from isapilib.models import ApiLogs


def safe_method(view_func):
    def wrapped_view(*args, **kwargs):
        try:
            return view_func(*args, **kwargs)
        except KeyError as e:
            return JsonResponse({
                'field': e.args[0],
                'message': f"This field is required."
            }, status=400)
        except SepaException as e:
            return JsonResponse({
                'field': 'Authentication',
                'message': str(e)
            }, status=401)

    return wrapped_view


def logger(interfaz, tipo):
    def decorador(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                try:
                    request = next((arg for arg in args if isinstance(arg, Request)), None)
                    log = ApiLogs()
                    log.iduser = request.user.pk
                    log.tipo = tipo
                    log.header = str(request.headers)
                    log.request = str(request.data)
                    log.response = str(e)
                    log.url = request.build_absolute_uri()
                    log.interfaz = interfaz
                    log.save()
                finally:
                    raise e

        return wrapper

    return decorador
