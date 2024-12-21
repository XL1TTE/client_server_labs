from django.shortcuts import render, redirect

from .models import Book
from .forms import BookForm


def book_archive(request):
    Book.objects
    books = Book.objects.all()
    context = {"Books": books}

    return render(request, "books_archive.html", context=context)

def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_archive')
    else:
        form = BookForm()

    context = {'form': form}
    return render(request, 'add_book.html', context)
