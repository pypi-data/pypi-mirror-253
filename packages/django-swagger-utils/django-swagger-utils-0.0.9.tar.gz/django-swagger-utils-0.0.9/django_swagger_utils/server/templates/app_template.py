import os
import re
import logging
from os import path
from django.core.management.base import BaseCommand
from django_swagger_utils.server.templates.app_config import APP_CONFIG
from django_swagger_utils.server.constants import APP_STRUCTURE, APP_BASE_FILES, INIT_FILE_NAME, \
APP_NAME_REGEX_PATTERN, APP_INIT_CONFIG, APP_FILE
from django_swagger_utils.server.exceptions.create_app import APP_NAME_VALIDATION_ERROR_MESSAGE, APP_CREATE_ERROR

class TemplateCommand(BaseCommand):
    def __init__(self, stdout=None, stderr=None, no_color=False):
        super(TemplateCommand, self).__init__(stdout, stderr, no_color)
        self.app_path = None
        self.parent_directory = None
        self.app = None
        self.app_name = None
        self.logger = logging.getLogger(__name__)

    def add_arguments(self, parser):
        parser.add_argument("--app", help="Command-specific option")

    def handle(self, app, app_name, **options):
        self.app = app
        self.app_name = app_name
        self.parent_directory = os.getcwd()
        self.app_path = path.join(self.parent_directory, app_name)

        try:
            if self._validate_app_name(app_name):
                content = APP_INIT_CONFIG.format(self.app_name, self.app_name)
                self._create_directory(self.app_path, content)
                self._create_subdirectory(self.app_path)
                self._create_app_files(self.app_path)
            else:
                self.logger.error(APP_NAME_VALIDATION_ERROR_MESSAGE)
        except OSError as e:
            self.logger.error(APP_CREATE_ERROR.format(e))
            os.rmdir(self.app_path)

    @staticmethod
    def _validate_app_name(app_name):
        pattern = r'{}'.format(APP_NAME_REGEX_PATTERN)
        return re.match(pattern, app_name)

    @staticmethod
    def _create_file(directory_path, file_name, content=''):
        with open(os.path.join(directory_path, file_name), 'w') as file:
            file.write(content)

    def _create_directory(self, directory_path, content=''):
        try:
            os.mkdir(directory_path)
            with open(os.path.join(directory_path, INIT_FILE_NAME), 'w') as file:
                file.write(content)
        except Exception:
            return Exception

    def _create_subdirectory(self, sub_directory):
        try:
            for module in APP_STRUCTURE:
                module_path = os.path.join(sub_directory, module)
                self._create_directory(module_path)
                for sub_module in APP_STRUCTURE.get(module):
                    for each_file in sub_module:
                        sub_module_path = os.path.join(module_path, each_file)
                        self._create_directory(sub_module_path)
        except Exception:
            return Exception

    def _create_app_files(self, app_directory):
        for app_file in APP_BASE_FILES:
            if app_file == "app.py":
                app_config_code = APP_CONFIG.replace("{{app}}", self.app_name)
                self._create_file(app_directory, app_file, app_config_code)
            else:
                self._create_file(app_directory, app_file)