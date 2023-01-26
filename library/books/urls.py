from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='books-home'),
    path('authors/', views.authors, name='books-authors'),
    path('authors/<int:id>/', views.showByAuthor, name='books-showByAuthor'),
    path('books/', views.books, name='books-books'),
    path('books/<int:id>/',views.show, name="books-show"),
]

handler404 = 'books.views.not_found_404'
# handler500 = 'books.views.server_error_500'