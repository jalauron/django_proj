from django.urls import path
from .views import BookListView, HomePageView, BookCreateView, BookUpdateView, BookDeleteView, BookDetailView, BookStatisticsView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),  # Home page
    path('books/', BookListView.as_view(), name='book_list'),  # List of books
    path('book/<int:pk>/', BookDetailView.as_view(), name='book_detail'),  # Book details
    path('book/new/', BookCreateView.as_view(), name='book_create'),  # Add a new book
    path('book/<int:pk>/edit/', BookUpdateView.as_view(), name='book_update'),
    path('book/<int:pk>/delete/', BookDeleteView.as_view(), name='book_delete'),
    path('books/statistics/', BookStatisticsView, name='book_statistics'),  # Statistics page
]
