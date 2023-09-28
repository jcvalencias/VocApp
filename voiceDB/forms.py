from django import forms
from .models import VocabDB 
from django.forms import formset_factory

class VocabDB_Form(forms.ModelForm):
    class Meta:
        model = VocabDB
        fields = ['French', 'Spanish', 'Example']

    French = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Escribe una palabra en francés'}),
        label='French'
    )
    Spanish = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Escribe la traducción'}),
        label='Spanish'
    )

    Example = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Escribe un ejemplo'}),
        label='Ejemplo'
    )

    # learning_rate = forms.FloatField(
    #     widget=forms.TextInput(attrs={'placeholder': '0.0'}),
    #     label='Learnin_rate'
    # )

class Bulk_form(forms.Form):
    
    text = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': 'Put your text here'}),
        required=False,
        label="Text"
    )

VocFormSet = formset_factory(VocabDB_Form, extra=0)