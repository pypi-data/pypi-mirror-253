import os
import importlib
from django.urls import re_path

url_patterns = []
views_dir = 'Users/views/'

for operation_id in os.listdir(views_dir):
    if not operation_id.endswith('.py'):
        module_name = operation_id
        full_module_path = f'Users.views.{module_name}.{operation_id}'
        try:
            module = importlib.import_module(full_module_path)
            view_func = getattr(module, operation_id, None)
            url_patterns.append(re_path(f'api/{operation_id}', view_func, name=operation_id))
        except ImportError as e:
            print(f"Failed to import module '{full_module_path}': {e}")
