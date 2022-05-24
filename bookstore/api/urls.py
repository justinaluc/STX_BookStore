from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from .views import get_api_spec, BookList, BookDetail, BookCreate

urlpatterns = [
    path('api_spec/', get_api_spec, name='api_specification'),
    path('books/', BookList.as_view(), {"action": "GET"}, name='book_list'),
    path('books/', BookCreate.as_view(), {"action": "POST"}, name='book_list'),
    path('books/<int:pk>/', BookDetail.as_view(), name='book_detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)