from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Book, Author
from .form import BorrowBook, UnborrowBook

# Create your views here.

def home(request):
    return render(request, "home.html")

def books(request):
    all_books = { 'books': Book.objects.all() }
    return render(request, "books.html", all_books)

def authors(request):
    all_authors = { 'authors': Author.objects.all() }
    return render(request, "authors.html", all_authors)

@login_required
def show(request, id):
    book = get_object_or_404(Book, pk=id)
    if request.method == 'POST':
        form = BorrowBook(request.POST)
        if form.is_valid():
            book.borrower = request.user
            book.save()
            return redirect('books-show', id=id)
    elif request.method == 'PUT':
        form = UnborrowBook(request.PUT)
        if form.is_valid():
            book.borrower = None
            book.save()
            return redirect('books-show', id=id)
    else:
        form = BorrowBook(initial={''})
    data = {'book': book, 'form': form}
    return render(request, "show.html", data)

def showByAuthor(request, id):
    author = get_object_or_404(Author, pk=id)
    data = {'author': author}
    return render(request, "showByAuthor.html", data)

def not_found_404(request, exception):
    data = {"err": exception}
    return render(request, '404.html', data)