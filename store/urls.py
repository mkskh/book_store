from django.urls import path
from . import views

app_name = 'store'

urlpatterns = [
    path('', views.index, name='index'),
    path('authors/', views.AuthorListView.as_view(), name='authors_list'),
    path('books/', views.BookListView.as_view(), name='books_list'),
    path('genres/', views.GenreListView.as_view(), name='genres_list'),
    path('contact/', views.contact, name='contact'),
    path('authors/create/', views.AuthorCreateView.as_view(), name='author_create'),
]