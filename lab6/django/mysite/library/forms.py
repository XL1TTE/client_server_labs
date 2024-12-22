
from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author'] 
        widgets = {
            'title': forms.TextInput(attrs={'class': 'rounded_green_input', 'placeholder': 'Название'}),
            'author': forms.TextInput(attrs={'class': 'rounded_green_input', 'placeholder': 'Автор'}),
        }
