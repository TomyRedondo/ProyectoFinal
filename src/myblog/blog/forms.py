from django import forms

class Mangaformulario(forms.Form):
    nombreDelManga = forms.CharField(max_length=100, required=False)
    autor = forms.CharField(max_length=100)
    email = forms.EmailField()