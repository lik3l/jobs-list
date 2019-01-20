from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse

from jobs.forms import JobForm
from jobs.models import Job
from .forms import LoginForm


def index(request):
    context = dict()

    if not request.user.is_authenticated:
        return redirect(reverse('login'))

    context['user'] = request.user
    context['jobs_list'] = Job.objects.all()

    return render(
        request,
        'core/index.html',
        context
    )


def login_view(request):
    login_form = LoginForm()
    errors = list()
    if request.method == 'POST':
        login_form = LoginForm(data=request.POST)
        if login_form.is_valid():
            cd = login_form.cleaned_data
            user = authenticate(request, email=cd['email'], password=cd['password'])
            if user is not None:
                login(request, user)
                return redirect(reverse('index'))
        login_form.fields['email'].widget.attrs['class'] = 'form-control is-invalid'

    return render(
        request,
        'core/login.html',
        {
            "login_form": login_form,
            "errors": errors,
        }
    )


def logout_view(request):
    logout(request)
    return redirect(reverse('index'))


@login_required
def create_job(request):
    job_form = JobForm()
    job_form.fields['worker'].initial = request.user
    if request.method == 'POST':
        job_form = JobForm(request.POST)
        if job_form.is_valid():
            job_form.save()
            return redirect(reverse('index'))
    return render(
        request,
        'core/create_job.html',
        {'job_form': job_form, 'user': request.user}
    )


@login_required
def finish_job(request, pk=None):
    try:
        job = Job.objects.get(pk=pk)
        job.status = Job.DONE
        job.save()
    except Job.DoesNotExist:
        pass
    return redirect(reverse('index'))


@login_required
def start_job(request, pk=None):
    try:
        job = Job.objects.get(pk=pk)
        job.status = Job.IN_WORK
        job.save()
    except Job.DoesNotExist:
        pass
    return redirect(reverse('index'))
