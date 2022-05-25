from django.urls import path

from .views import get_api_spec

urlpatterns = [
    path('api_spec/', get_api_spec, name='api_specification'),
]
