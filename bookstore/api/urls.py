from django.urls import path

from .views import BookApiView

urlpatterns = [
    path('books/', BookApiView.as_view(), name='api_book_list'),
]