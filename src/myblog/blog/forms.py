from django import forms

class Mangaformulario(forms.Form):
    nombreDelManga = forms.CharField(max_length=20, required=False)
    autor = forms.CharField(max_length=20)
    email = forms.EmailField()