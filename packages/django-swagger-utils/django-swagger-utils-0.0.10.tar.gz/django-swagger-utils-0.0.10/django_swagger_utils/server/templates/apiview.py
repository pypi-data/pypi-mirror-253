
__all__ = ['API_VIEW_TEMPLATE', 'API_URL_TEMPLATE']


API_URL_TEMPLATE = """from django.conf.urls import include, url
from {{ app }} import views


urlpatterns = [
{% for model in models %}
  url(r'^{{ model|lower }}/(?P<id>[0-9]+)/$', views.{{ model }}APIView.as_view()),
  url(r'^{{ model|lower }}/$', views.{{ model }}APIListView.as_view()),
{% endfor %}
]
"""


API_VIEW_TEMPLATE = """
import jwt
from rest_framework.pagination import PageNumberPagination
from django.conf import settings
from django_swagger_utils.server.validators.token_validator import ValidateToken

class {{ operationId }}(**args, **kwargs):
    
    access_token = ''
    http_authorization = args[0].META.get('HTTP_AUTHORIZATION')
    if http_authorization is not None:
        token = http_authorization[len("Bearer "):]
        validator_class = ValidateToken(token)
        if validator_class.validate_token(token):
            http_source = args[0].META.get("HTTP_X_SOURCE")
            access_token = token.split(" ")[1]
            kwargs.update({"access_token": access_token, 'source': http_source})
            return HttpResponse("Authentication successful")
        
        elif http_authorization.startswith("Basic "):
            base64_credentials = http_authorization[len("Basic "):]
            credentials = base64.b64decode(base64_credentials).decode("utf-8")
            username, password = credentials.split(":")
            # Perform validation of username and password here
            if username == "valid_username" and password == "valid_password":
                return HttpResponse("Authentication successful")
        return HttpResponse("Authentication failed", status=401)
        
    
    from .api_wrapper import api_wrapper
    response_object = api_wrapper(*args, **kwargs)

    allowed_primitive_types = [False, str, int, float]
    from functools import reduce  # pylint: disable=redefined-builtin
    if response_object is None:
        from django.http.response import HttpResponse
        response_object = HttpResponse()

    elif reduce((lambda a, b: a or isinstance(response_object, b)),
                allowed_primitive_types):
        from django.http.response import HttpResponse
        response_object = HttpResponse(str(response_object))

    return response_object
"""