from django.shortcuts import render
from django.db.models import Count
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Book

# Home page view
class HomePageView(TemplateView):
    template_name = 'myapp/home.html'

# Book List View
class BookListView(ListView):
    model = Book
    template_name = 'myapp/book_list.html'
    context_object_name = 'books'

# Book Detail View
class BookDetailView(DetailView):
    model = Book
    template_name = 'myapp/book_detail.html'
    context_object_name = 'book'

# Book Create View
class BookCreateView(CreateView):
    model = Book
    fields = ['title', 'author', 'description', 'published_date', 'isbn', 'image']
    template_name = 'myapp/book_form.html'
    success_url = '/books/'

# Book Update View
class BookUpdateView(UpdateView):
    model = Book
    fields = ['title', 'author', 'description', 'published_date', 'isbn', 'image']
    template_name = 'myapp/book_form.html'
    success_url = '/books/'

# Book Delete View
class BookDeleteView(DeleteView):
    model = Book
    template_name = 'myapp/book_confirm_delete.html'
    success_url = reverse_lazy('book_list')

# Book Statistics View
def BookStatisticsView(request):
    total_books = Book.objects.count()  # Total number of books
    # Count books by author
    books_by_author = Book.objects.values('author').annotate(author_count=Count('author'))
    # Count books by published year
    books_by_year = Book.objects.values('published_date__year').annotate(year_count=Count('published_date'))

    context = {
        'total_books': total_books,
        'books_by_author': books_by_author,
        'books_by_year': books_by_year,
    }

    return render(request, 'myapp/book_statistics.html', context)
