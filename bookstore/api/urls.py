from django.urls import path

from .views import get_api_spec, BookApiView

urlpatterns = [
    path('api_spec/', get_api_spec, name='api_specification'),
    path('books/', BookApiView.as_view(), name='api_book_list_class'),
]