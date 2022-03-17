from django import forms
from .models import Contacts


class ContactsForms(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), required=True)
    middle_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), required=True)
    alias = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), required=True)
    phone = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), required=True)

    class Meta:
        model = Contacts
        fields = ['name', 'middle_name', 'last_name', 'alias', 'phone']