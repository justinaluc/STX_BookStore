from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from .views import BookListView, home, BookList, BookDetail, BookCreate


urlpatterns = [
    path('bookstore/', BookListView.as_view(), name='book_list'),
    path('', home, name='home'),
    path('books/', BookList.as_view(), {"action": "GET"}, name='book_list_api'),
    path('books/', BookCreate.as_view(), {"action": "POST"}, name='book_create'),
    path('books/<int:pk>/', BookDetail.as_view(), name='book_detail'),
]