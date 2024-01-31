from django.http import HttpResponse, HttpRequest
from django_swagger_utils.server.decorators.interface_decorator import validate_decorator
from .validator_class import ValidatorClass

@validate_decorator(ValidatorClass)
def api_wrapper(*args, **kwargs):
    # ---------MOCK IMPLEMENTATION---------
    if HttpRequest:
        return {"message": "success", "status": 200}
    return {"message": "success", "status": 400}
