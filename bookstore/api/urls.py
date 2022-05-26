from django.urls import path

from .views import get_api_spec, find_volume

urlpatterns = [
    path('api_spec/', get_api_spec, name='api_specification'),
    path('import/', find_volume, name='import_books'),
]
