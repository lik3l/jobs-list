from django import forms
from django.contrib.auth import get_user_model

from .models import Job, Company, Material

User = get_user_model()


class JobForm(forms.ModelForm):
    worker = forms.ModelChoiceField(queryset=User.objects.all(), widget=forms.HiddenInput())

    class Meta:
        model = Job
        fields = '__all__'


class CompanyForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    phone = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    contact_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    address = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 3}))

    class Meta:
        model = Company
        fields = '__all__'


class MaterialForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    default_price = forms.FloatField(widget=forms.NumberInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Material
        fields = '__all__'
