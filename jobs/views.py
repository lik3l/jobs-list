from django.contrib.auth.decorators import login_required
from django.shortcuts import render

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
