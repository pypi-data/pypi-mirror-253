from django.urls import path, include
from django.contrib import admin
from django.apps import apps

urlpatterns = [
    path(r'^admin/', admin.site.urls),
    # Add more URL patterns as needed
]

for app_config in apps.get_app_configs():
    try:
        urls_module = __import__(app_config.name + '.urls', fromlist=['url_patterns'])
        app_urlpatterns = getattr(urls_module, 'url_patterns', [])
        urlpatterns += app_urlpatterns
    except ImportError:
        pass