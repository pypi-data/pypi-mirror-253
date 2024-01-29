from django.urls import path, include
from django.contrib import admin
from django.conf import settings
from Testing.urls import url_patterns

urlpatterns = [
    path(r'^admin/', admin.site.urls),
    # Add more URL patterns as needed
]

urlpatterns.extend(url_patterns)

