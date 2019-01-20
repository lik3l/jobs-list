from django import forms
from django.contrib.auth import get_user_model

from .models import Job, Company

User = get_user_model()


class JobForm(forms.ModelForm):
    worker = forms.ModelChoiceField(queryset=User.objects.all(), widget=forms.HiddenInput())

    class Meta:
        model = Job
        fields = '__all__'


class CompanyForm(forms.ModelForm):

    class Meta:
        model = Company
        fields = '__all__'
