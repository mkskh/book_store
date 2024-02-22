from typing import Any
from django.http import HttpResponse
from .models import Author, Book, Genre, StoreManager, StoreLocation, Contact
from django.views import View
from django.urls import reverse
from django.shortcuts import render, redirect
from .forms import ContactForm, BookForm, AuthorForm
from django.views.generic.edit import FormView
from django.views.generic import TemplateView


def index(request):
    num_of_book = Book.objects.all().count()
    return render(request, "store/index.html", {"num_of_book": num_of_book})


class AuthorListView(View):

    def get(self, request):
        authors = Author.objects.all()

        return render(request, "store/author_list.html", {"authors": authors})
    

class AuthorCreateView(FormView):
    template_name = "store/create_author.html"
    form_class = AuthorForm
    success_url = "/store/authors/"

    def form_valid(self, form):
        form.save()
        return super(AuthorCreateView, self).form_valid(form)


class BookListView(View):

    def get(self, request):
        books = Book.objects.all()
        form = BookForm()
        return render(request, 'store/book_list.html', {
            "books": books, "form": form
        })
    def post(self, request):
        form = BookForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('store:book_list')
        else:
            return render(request, "store/book_list.html", {
                "form": form, "books": books
                })   
    

# class GenreListView(View):

#     def get(self, request):
#         genres = Genre.objects.all()
#         content = ''

#         for genre in genres:
#             new_genre = f"<li>{genre}</li>"
#             content += new_genre
        
#         return HttpResponse(content)

class GenreListView(TemplateView):
    template_name = "store/genre_list.html"
    
    def get_context_data(self, *args, **kwargs):
        context = super(GenreListView, self).get_context_data(*args, **kwargs)
        context['genres'] = Genre.objects.all()
        context['random'] = "Just some random text"
        return context


def contact(request):
    # create the form object/instance
    form = ContactForm()
    # send the form as context to the template
    if request.method == "GET":
        return render(request, "store/contact.html", {'form': form})

    # Saving to DB
    elif request.method == "POST":
        # receive the form using a POST request
        form = ContactForm(request.POST)

        # Validate the form inputs
        if form.is_valid():
            # Save inputs to DB
            new_contact = Contact(name=form.cleaned_data['name'], email=form.cleaned_data['email'],
                                phone_number=form.cleaned_data['phone_number'], message=form.cleaned_data['message'])
            new_contact.save()
            return redirect('store:index')
        else:
            return render(request, 'store/contact.html', {"form": form})


    