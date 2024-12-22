from django.urls import path

from . import views

urlpatterns = [
    path('book_archive', views.book_archive, name="book_archive"),
    path('add_book', views.add_book_form, name="load_add_book_form")
]
