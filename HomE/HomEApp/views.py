from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_protect
from django.contrib import messages, auth
from django.contrib.auth import authenticate

from .models import Home, Tenent, Rent


def home(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def services(request):
    return render(request, 'services.html')


def login(request):
    return render(request, 'login.html')


@csrf_protect
def get_authenticate(request):
    user = auth.authenticate(username=request.POST['email'], password=request.POST['password'])
    if user is not None:
        auth.login(request,user)
        return render(request, 'rent.html')
    else:
        messages.info(request, 'Invalid Email or Password')
        return redirect('login')


def search(request):
    print(request.GET['search'])
    return redirect('rent_detail')


@csrf_protect
def rent_detail(request):
    if request.user.is_authenticated:
        rent_details = Rent.objects.all()
        return render(request, 'rent.html', {'rent_details': rent_details})
    else:
        return render(request, 'login.html')




@csrf_protect
def tenent_detail(request):
    if request.user.is_authenticated:
        tenent_details = Tenent.objects.all()
        return render(request, 'tenent.html', {'tenent_details': tenent_details})
    else:
        return render(request, 'login.html')


@csrf_protect
def home_detail(request):
    if request.user.is_authenticated:
        home_details = Home.objects.all()
        return render(request, 'home_detail.html', {'home_details': home_details})
    else:
        return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return render(request, 'login.html')