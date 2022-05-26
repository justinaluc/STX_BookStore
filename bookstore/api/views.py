import requests
from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view

from bookstore.settings import GOOGLE_API_KEY

from .forms import AuthorForm


@api_view(['GET'])
def get_api_spec(request):
    """
    gives a rigid specification data about required api project version
    """
    spec = {
        "info": {
            "version": "2022.05.16"
            }
        }
    return Response(spec)


def volume_import(name):
    """use parameter 'name' to search books by author in GOOGLE BOOKS API"""
    google_api_url = "https://www.googleapis.com/books/v1/volumes?q=inauthor:" \
                     f"{name}&key={GOOGLE_API_KEY}"

    response = requests.get(google_api_url)
    response.raise_for_status()
    import_data = response.json()
    imported = import_data['totalItems']
    books_data = []
    for item in import_data['items']:
        book = {
            'external_id': item['id'],
            'title': item['volumeInfo']['title'],
            'authors': item['volumeInfo'].get('authors'),
            'published_year': item['volumeInfo']['publishedDate'][:4],
            'thumbnail': None
        }
        if 'imageLinks' in item['volumeInfo']:
            book['thumbnail'] = item['volumeInfo']['imageLinks']['thumbnail']
        books_data.append(book)
    return imported, books_data


@api_view(['GET', 'POST'])
def find_volume(request):
    """use Django form to POST author's name in volume_import function
    >>request.data from Django Rest Framework supposed to be used, but do not know how yet<<"""
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            author = form.cleaned_data
            if author['author'].isalpha():
                imported, books_data = volume_import(author['author'])
                result = {"imported": imported}
                """books_data has to be used to check local database 
                and create or update instances of book model if necessary;
                >>but this functionality is not ready yet<< """
                return Response(result)

    if request.method == 'GET':
        form = AuthorForm()

    return render(request, "api/author_form.html", {'form': form})

