from django.http import HttpResponse
from django.shortcuts import render
from django.template import RequestContext, loader
from django.views.decorators.csrf import requires_csrf_token
from django.views.decorators.csrf import csrf_protect


def home(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def services(request):
    return render(request, 'services.html')


def login(request):
    return render(request, 'login.html', {'message': 'LOGIN', 'screen': 'LOGIN'})


@csrf_protect
def authenticate(request):
    csrfContext = RequestContext(request)
    if request.POST['email'] == "sheikhjebran@gmail.com" and request.POST['password'] == "admin":
        return render(request, 'rent.html')
    else:
        return render(request, 'login.html', {'message': 'Invalid Email or Password', 'screen': 'LOGIN'})


def rent_detail(request):
    return render(request, 'rent.html')


def tenent_detail(request):
    return render(request, 'tenent.html')


def home_detail(request):
    return render(request, 'home_detail.html')
