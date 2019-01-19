from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

from .forms import LoginForm


def index(request):
    context = dict()

    context['login_form'] = LoginForm()
    context['user'] = request.user

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
                return redirect('index')
        login_form.fields['email'].widget.attrs['class'] = 'form-control is-invalid'

    return render(
        request,
        'core/login.html',
        {
            "login_form": login_form,
            "errors": errors,
        }
    )
