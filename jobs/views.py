from django.contrib.auth.decorators import login_required
from django.db.models import ProtectedError
from django.shortcuts import render, redirect
from django.urls import reverse

from .forms import CompanyForm, MaterialForm
from .models import Company, Material


@login_required
def company_list(request):
    context = dict()
    companies = Company.objects.all()

    context['user'] = request.user
    context['companies'] = companies
    context['view_name'] = request.resolver_match.url_name

    return render(
        request,
        'jobs/company_list.html',
        context
    )


@login_required
def add_company(request):
    company_form = CompanyForm()
    if request.method == 'POST':
        company_form = CompanyForm(request.POST)
        if company_form.is_valid():
            company_form.save()
            return redirect(reverse('company_list'))

    return render(
        request,
        'jobs/add_company.html',
        dict(user=request.user, company_form=company_form)
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
                return redirect(reverse('company_list'))
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


@login_required
def company_delete(request, pk=None):
    try:
        company = Company.objects.get(pk=pk)
        company.delete()
    except (Company.DoesNotExist, ProtectedError):
        pass
    return redirect(reverse('company_list'))


@login_required
def material_list(request):
    context = dict()
    materials = Material.objects.all()

    context['user'] = request.user
    context['materials'] = materials
    context['view_name'] = request.resolver_match.url_name

    return render(
        request,
        'jobs/material_list.html',
        context
    )


@login_required
def add_material(request):
    material_form = MaterialForm()
    if request.method == 'POST':
        material_form = MaterialForm(request.POST)
        if material_form.is_valid():
            material_form.save()
            return redirect(reverse('material_list'))

    return render(
        request,
        'jobs/add_material.html',
        dict(user=request.user, material_form=material_form)
    )


@login_required
def material_detail(request, pk=None):
    context = dict()

    try:
        material = Material.objects.get(pk=pk)
        if request.method == 'POST':
            material_form = MaterialForm(request.POST, instance=material)
            if material_form.is_valid():
                material_form.save()
                return redirect(reverse('material_list'))
        else:
            material_form = MaterialForm(instance=material)

    except Material.DoesNotExist:
        return redirect(reverse('material_list'))

    context['material'] = material
    context['user'] = request.user
    context['material_form'] = material_form

    return render(
        request,
        'jobs/material_detail.html',
        context
    )


@login_required
def material_delete(request, pk=None):
    try:
        material = Material.objects.get(pk=pk)
        material.delete()
    except (Company.DoesNotExist, ProtectedError):
        pass
    return redirect(reverse('material_list'))
