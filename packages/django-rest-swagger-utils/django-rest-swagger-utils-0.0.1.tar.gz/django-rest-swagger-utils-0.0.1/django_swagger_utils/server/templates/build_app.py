import json
import os
import time
import shutil
import logging
import threading
from django.core.management.base import BaseCommand
from django_swagger_utils.server.generators.app_view_generator import *
from django_swagger_utils.server.constants.paths import API_SPEC_PATH, VIEWS_ABS_PATH, API_SPEC_FILE_NAME
from django_swagger_utils.server.exceptions.create_app import REVERT_GENERATED_APP_FILES, DELETE_GENERATED_APP_FILES_FAILED

class TemplateCommand(BaseCommand):
    def __init__(self, stdout=None, stderr=None, no_color=False):
        super(TemplateCommand, self).__init__(stdout, stderr, no_color)
        self.app_path = None
        self.app_name = None
        self.parent_directory = None
        self.swagger_spec = {}
        self.url_paths = None
        self.app_config = None
        self.logger = logging.getLogger(__name__)
        self.views_completed = False

    @staticmethod
    def add_arguments(parser):
        parser.add_argument("--app", help="Command-specific option")

    def _generate_views_with_threading(self):
        try:
            self._generate_views()
        except OSError:
            subdirectories = [d for d in os.listdir(self.app_path) if
                              os.path.isdir(os.path.join(self.app_path, d))]

            for subdirectory in subdirectories:
                subdirectory_path = os.path.join(self.app_path, subdirectory)

                try:
                    shutil.rmtree(subdirectory_path)
                    self.logger.error(REVERT_GENERATED_APP_FILES.format(self.app_name))
                except OSError as e:
                    self.logger.error(DELETE_GENERATED_APP_FILES_FAILED.format(e))
        time.sleep(5)
        self.views_completed = True

    def handle(self, app, app_name, app_config, **options):
        self.app_name = app_name
        self.app_config = app_config
        self.parent_directory = os.path.abspath(app_name)
        self.app_path = VIEWS_ABS_PATH.format(self.parent_directory)
        self.swagger_spec = self._get_api_spec()
        swagger_spec_is_valid = self._validate_swagger_spec(self.swagger_spec)

        if swagger_spec_is_valid:
            # Start the _generate_views_with_threading thread
            thread = threading.Thread(target=self._generate_views_with_threading, args=())
            thread.start()
            print("generating views...")

            # Wait for _generate_views_with_threading to complete
            thread.join()
            
            # Start the _generate_app_urls thread only if _generate_views_with_threading has completed
            if self.views_completed:
                print("generating app urls...")
                self._generate_app_urls()

    def _get_api_spec(self):
        file_path = API_SPEC_PATH.format(self.app_name)
        with open(os.path.join(file_path, API_SPEC_FILE_NAME), 'r') as file:
            file_contents = file.read()
        return file_contents

    def _validate_swagger_spec(self, swagger_spec):
        swagger_data = json.loads(swagger_spec)
        try:
            self.url_paths = swagger_data.get('paths')
            return True
        except AttributeError:
            return False

    def _generate_views(self):
        generator = APIViewGenerator(self.app_config, force=False)
        generator.generate_views(self.url_paths)

    def _generate_app_urls(self):
        urls_generator = APIViewGenerator(self.app_config, force=False)
        urls_generator.generate_app_urls(self.url_paths)
