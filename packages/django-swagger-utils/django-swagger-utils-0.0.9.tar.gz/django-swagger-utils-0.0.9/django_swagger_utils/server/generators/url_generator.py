import os
import time
import threading
import importlib
from django.urls import path, re_path
from django_swagger_utils.server.templates.app_urls import APP_URLS
from django_swagger_utils.server.constants.paths import VIEWS_ABS_PATH


class BaseURLPatterns:
    def __init__(self, app_config, force):
        self.app_name = app_config.name
        self.url_patterns = []

    def generate_url_patterns(self, url_path, http_method, operation_details):
        operation_id = operation_details.get('operationId')
        module_name = "{}.views.{}.{}".format(self.app_name, operation_id, operation_id)
        try:
            module = importlib.import_module(module_name)
            view_func = getattr(module, operation_id)
            if http_method == 'get':
                print("url_path: ",url_path)
                self.url_patterns.append(
                    path(url_path, view_func, name=operation_id)
                )
            elif http_method == 'post':
                self.url_patterns.append(
                    path(url_path, view_func, name=operation_id)
                )
        except ImportError as e:
            print("import error: ", str(e))

class URLPatternsGenerator(BaseURLPatterns):
    def __init__(self, app_config, force):
        # module_name = '{}.app'.format(app_name)
        # module = importlib.import_module(module_name)
        # app_config = getattr(module, '{}AppConfig'.format(app_name))
        super(URLPatternsGenerator, self).__init__(app_config, force)
        