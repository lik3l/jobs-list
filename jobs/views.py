from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse

from .forms import CompanyForm
from .models import Company, Material


@login_required
def company_list(request):
    context = dict()
    companies = Company.objects.all()

    context['user'] = request.user
    context['companies'] = companies

    return render(
        request,
        'jobs/company_list.html',
        context
    )


@login_required
def company_detail(request, pk=None):
    context = dict()

    try:
        company = Company.objects.get(pk=pk)
        if request.method == 'POST':
            company_form = CompanyForm(request.POST, instance=company)
            if company_form.is_valid():
                company_form.save()
        else:
            company_form = CompanyForm(instance=company)

    except Company.DoesNotExist:
        return redirect(reverse('company_list'))

    context['company'] = company
    context['user'] = request.user
    context['company_form'] = company_form

    return render(
        request,
        'jobs/company_detail.html',
        context
    )
