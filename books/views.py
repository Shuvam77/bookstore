from turtle import title
from django.db import models
from django.db.models import Q

from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    PermissionRequiredMixin
)

from django.views.generic import ListView, DetailView

from .models import Book

# Create your views here.


class BookListView(LoginRequiredMixin ,ListView):
    model = Book
    context_object_name = 'book_list'
    template_name = 'books/book_list.html'
    login_url = 'account_login'


class BookDetailView(LoginRequiredMixin,PermissionRequiredMixin ,DetailView):
    model = Book
    context_object_name = 'book'
    template_name = 'books/book_detail.html'
    login_url = 'account_login'
    permission_required = 'books.special_status'

class SearchResultsListView(ListView):
    model = Book
    context_object_name = 'book_list'
    template_name = 'books/search_result.html'
    # queryset = Book.objects.filter(title__icontains='professionals')

    def get_queryset(self):
        query = self.request.GET.get('query')
        return Book.objects.filter(
            Q(title__icontains=query) | Q(title__icontains=query)
        )
