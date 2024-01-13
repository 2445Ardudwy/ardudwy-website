from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('first_name', 'last_name', 'email', 'telephone', 'purpose', 'message')

        widgets = {
            'first_name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name', 'type':'text', 'id':'validationCustom01'}),
            'last_name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last Name'}),
            'email': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email Address', 'type':'email'}),
            'telephone': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Telephone number'}),
            'purpose': forms.Select(attrs={'class':'form-control form-select'}),
            'message': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Message'}),
        }