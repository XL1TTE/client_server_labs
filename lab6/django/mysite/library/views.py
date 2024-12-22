from django.shortcuts import render, redirect

from .models import Book
from .forms import BookForm


def book_archive(request):
    Book.objects
    books = Book.objects.all()
    context = {"Books": books}

    return render(request, "books_archive.html", context=context)


def add_book_form(request):
    if request.method == 'POST':
        add_book(request=request)
        return redirect('book_archive')
    else:
        form = BookForm()
        context = {'form': form}
        return render(request, 'add_book_form.html', context)

def add_book(request):
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
