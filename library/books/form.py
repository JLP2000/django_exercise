from django import forms
from .models import Book

class BorrowBook(forms.ModelForm):
    class Meta:
        model = Book
        field = ['borrower']
        widget = {'borrower': forms.HiddenInput()}

class UnborrowBook(forms.ModelForm):
    class Meta:
        model = Book
        field = ['borrower']
        widget = {'borrower': forms.HiddenInput()}