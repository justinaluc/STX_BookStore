from django import forms
from django.forms import ModelForm

from books.models import Author


class AuthorForm(forms.Form):
    """
    form to look for author's books in Google API
    """
    author = forms.CharField(max_length=255, required=True,
                             widget=forms.TextInput(attrs={'placeholder': "author's name..."}))

