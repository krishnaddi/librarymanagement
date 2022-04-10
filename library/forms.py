from django import forms
from .models import Library
class LibraryForm(forms.ModelForm):
    class Meta:
        model=Library
        fields='__all__'
        labels={
            'name':'Book Name',
            'author':'Book Author',
            'price':'Book Price(₹)'
        }