import json
import shutil
import os.path
import logging
from django.template import Template, Context
from django_swagger_utils.server.templates.app_urls import APP_URLS
from django_swagger_utils.server.templates.views import VIEWS_TEMPLATE
from django_swagger_utils.server.templates.apiview import API_VIEW_TEMPLATE
from django_swagger_utils.server.templates.serializer import SERIALIZER_TEMPLATE
from django_swagger_utils.server.templates.validator_class import VALIDATOR_CLASS
from django_swagger_utils.server.templates.api_wrapper import API_WRAPPER_TEMPLATE
from django_swagger_utils.server.generators.url_generator import URLPatternsGenerator
from django_swagger_utils.server.templates.request_response_mocks import REQUEST_RESPONSE_MOCKS
from django_swagger_utils.server.templates.modelviewset import MODEL_URL_TEMPLATE, MODEL_VIEW_TEMPLATE
from django_swagger_utils.server.constants.paths import VIEWS_ABS_PATH, INIT_FILE_NAME, TESTS_DIRECTORY_NAME, \
API_SPEC_OPERATION_ID, API_SPEC_RESPONSES
from django_swagger_utils.server.exceptions.view_generator_exceptions import OVERWRITE_FILENAME, CLEANUP_COMPLETED, \
CLEANUP_FAILED, VIEWS_GENERATION_FAILED
from django_swagger_utils.server.constants.view_structure import VIEW_STRUCTURE, API_WRAPPER_FILE, \
REQUEST_RESPONSE_MOCKS_FILE,VALIDATOR_CLASS_FILE

__all__ = ['BaseGenerator', 'APIViewGenerator', 'ViewSetGenerator',
           'FunctionViewGenerator', 'ModelViewSetGenerator']


class BaseGenerator(object):

    def __init__(self, app_config, force):
        self.app_config = app_config
        self.force = force
        self.name = app_config.name
        self.logger = logging.getLogger(__name__)
        # self.serializer_template = Template(SERIALIZER_TEMPLATE)
        
    def create_init_file(self, directory, content=''):
        with open(os.path.join(directory, INIT_FILE_NAME), 'w') as file:
            file.write(content)

    def generate_views(self, url_paths):
        views_path = VIEWS_ABS_PATH.format(os.path.abspath(self.name))
        for url_path, path_details in url_paths.items():
            for http_method, operation_details in path_details.items():
                try:
                    operationId = operation_details.get(API_SPEC_OPERATION_ID)
                    views_directory_path = os.path.join(views_path, operationId)
                    tests_directory_path = os.path.join(views_directory_path, TESTS_DIRECTORY_NAME)
                    self.create_python_directory(views_directory_path)
                    self.create_python_directory(tests_directory_path)
                    self.generate_views_required_files(views_directory_path, operation_details.get(API_SPEC_RESPONSES), operationId)
                except Exception as e:
                    self.logger.error(VIEWS_GENERATION_FAILED.format(Exception.__dict__))
                    self.cleanup_generated_files(views_directory_path)
        
    def write_file(self, content, filename, directory):
        try:
            name = os.path.join(directory, filename)
            if os.path.exists(name) and not self.force:
                msg = OVERWRITE_FILENAME % filename
                prompt = input  # python3
                response = prompt(msg)
                if response != "y":
                    return False
            with open(name, 'w') as file:
                file.write(content)
            return True
        except Exception:
            return Exception
    
    def generate_views_required_files(self, view_path, responses, operationId):
        for key, value in VIEW_STRUCTURE.items():
            view_directory = os.path.join(view_path, value)
            try:
                if value == API_WRAPPER_FILE:
                    self.generate_api_wrapper(view_path, value, operationId)
                elif value == REQUEST_RESPONSE_MOCKS_FILE:
                    self.generate_request_response_mocks(view_path, value, responses)
                elif value == VALIDATOR_CLASS_FILE:
                    self.generate_validator_class(view_path, value)
            except Exception:
                return Exception
        self.generate_view_function("{}.py".format(operationId), view_path, operationId)
        return True

    def generate_view_function(self, file, view_directory, operationId):
        return self.write_file(VIEWS_TEMPLATE.replace("{{operation_id}}", operationId), file, view_directory)
    
    def generate_api_wrapper(self, view_directory, file, operation_id):
        return self.write_file(API_WRAPPER_TEMPLATE, file, view_directory)
    
    def generate_request_response_mocks(self, view_directory, file, responses):
        request_response_content = REQUEST_RESPONSE_MOCKS.replace("{{request_response}}", json.dumps(responses))
        return self.write_file(request_response_content, file, view_directory)
    
    def generate_validator_class(self, view_directory, file):
        return self.write_file(VALIDATOR_CLASS, file, view_directory)
    
    def create_python_directory(self, directory_path, content=''):
        try:
            os.mkdir(directory_path)
            self.create_init_file(directory_path, content)
        except Exception:
            return Exception
    
    def cleanup_generated_files(self, directory_path):
        try:
            if os.path.exists(directory_path):
                self.logger.error(CLEANUP_COMPLETED.format(directory_path))
                shutil.rmtree(directory_path)
        except Exception as e:
            self.logger.error(CLEANUP_FAILED.format(str(e)))

    def generate_app_urls(self, url_paths):
        generate_url_patterns_instance = URLPatternsGenerator(self.app_config, force=False)
        for url_path, path_details in url_paths.items():
            for http_method, operation_details in path_details.items():
                try:
                    generate_url_patterns_instance.generate_url_patterns(url_path, http_method, operation_details)
                except Exception as e:
                    self.logger.error(VIEWS_GENERATION_FAILED.format(str(e)))
                    # self.cleanup_generated_files(views_directory_path)
        app_path = os.path.abspath(self.name)
        app_urls_path = os.path.join(app_path, 'urls.py')
        for url in generate_url_patterns_instance.url_patterns:
            print("url: ", url)
            
        app_urls_template = APP_URLS.replace("{{url_patterns}}", str(generate_url_patterns_instance.url_patterns))
        print("url_patterns",generate_url_patterns_instance.url_patterns)
        with open(app_urls_path, 'w') as file:
                file.write(app_urls_template)
                    

class APIViewGenerator(BaseGenerator):

    def __init__(self, app_config, force):
        super(APIViewGenerator, self).__init__(app_config, force)
        self.view_template = Template(API_VIEW_TEMPLATE)
        # self.url_template = Template(API_URL)


class ViewSetGenerator(BaseGenerator):

    def __init__(self, app_config, force):
        super(ViewSetGenerator, self).__init__(app_config, force)


class FunctionViewGenerator(BaseGenerator):

    def __init__(self, app_config, force):
        super(FunctionViewGenerator, self).__init__(app_config, force)
        self.view_template = Template(VIEWS_TEMPLATE_TEMPLATE)
        # self.url_template = Template(FUNCTION_URL)


class ModelViewSetGenerator(BaseGenerator):

    def __init__(self, app_config, force):
        super(ModelViewSetGenerator, self).__init__(app_config, force)
        self.view_template = Template(MODEL_VIEW_TEMPLATE)
        self.url_template = Template(MODEL_URL_TEMPLATE)