from datetime import datetime

from django import forms
from django.contrib.auth import get_user_model

from .models import Job, Company, Material, CompanyPrice

User = get_user_model()


class JobForm(forms.ModelForm):
    worker = forms.ModelChoiceField(queryset=User.objects.all(), widget=forms.HiddenInput())

    client = forms.ModelChoiceField(queryset=Company.objects.all(),
                                    widget=forms.Select(attrs={'class': 'form-control'}))
    material = forms.ModelChoiceField(queryset=Material.objects.all(),
                                      widget=forms.Select(attrs={'class': 'form-control'}))
    ends = forms.DateField(widget=forms.DateInput(
        attrs={'class': 'form-control', 'type': 'date'}
    ), initial=datetime.now().strftime('%Y-%m-%d'))
    status = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-control'}), choices=Job.STATUSES)
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    width = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    height = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    rate = forms.FloatField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    payment = forms.FloatField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    price = forms.FloatField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    qty = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}))

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


class CompanyPriceForm(forms.ModelForm):
    company = forms.ModelChoiceField(
        queryset=Company.objects.all(),
        widget=forms.HiddenInput()
    )
    material = forms.ModelChoiceField(
        queryset=Material.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    price = forms.FloatField(widget=forms.NumberInput(attrs={'class': 'form-control'}))

    class Meta:
        model = CompanyPrice
        fields = '__all__'
