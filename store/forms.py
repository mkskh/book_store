from django import forms
from .models import Book, Author


class ContactForm(forms.Form):
    name = forms.CharField(max_length=200)
    email = forms.EmailField(max_length=200)
    phone_number = forms.CharField(max_length=200)
    message = forms.CharField(widget=forms.Textarea(attrs={"rows": "10"}))


class BookForm(forms.ModelForm):
    dummy_field = forms.CharField(max_length=10)
    class Meta:
        model = Book
        fields = ['title', 'author', 'summary', 'isbn', 'genre', 'date_of_publishing', 'in_stock', 'price']
        exclude = ['discount', 'slug']


class AuthorForm(forms.ModelForm):
    date_of_birth = forms.DateField(widget=forms.DateInput(format="%Y-%m-%d", attrs={"type": "date"}))

    class Meta:
        model = Author
        exclude = ["created_on", "last_updated"]