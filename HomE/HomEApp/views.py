from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_protect
from django.contrib import messages, auth
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer

from .models import Home, Tenent, Rent
import datetime


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
        return rent_detail(request)
    else:
        messages.info(request, 'Invalid Email or Password')
        return redirect('login')


def search(request):
    print(request.GET['search'])
    return redirect('rent_detail')


@csrf_protect
def rent_detail(request,page=10, current_page=1):
    if request.user.is_authenticated:
        rent_details = Rent.objects.all().order_by('-id')[:page * current_page]
        return render(request, 'rent.html', 
                      {'rent_details': rent_details,
                       'page_count': current_page}
                      )
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


def home_detail_modify(request,ID):
    home_detail_obj = Home.objects.get(pk=ID)
    print("home=",home_detail_obj.home_name)
    print("home=", home_detail_obj.home_location)
    return render(request,'home_detail_modify.html',{'home_detail': home_detail_obj})


def tenent_detail_modify(request, ID):
    tenent_detail_obj = Tenent.objects.get(pk=ID)
    print("Started date =", tenent_detail_obj.tenent_start_date)
    print("Started date =", type(tenent_detail_obj.tenent_start_date))
    return render(request, 'tenent_detail_modify.html', {'tenent_detail': tenent_detail_obj})


def rent_detail_modify(request, ID):
    rent_detail_obj = Rent.objects.get(pk=ID)
    return render(request, 'rent_detail_modify.html', {'rent_detail': rent_detail_obj})


def delete_home_detail(request, ID):
    home_detail_obj = Home.objects.get(pk=ID)
    home_detail_obj.delete()
    return home_detail(request)


def delete_tenent_detail(request, ID):
    tenent_detail_obj = Tenent.objects.get(pk=ID)
    tenent_detail_obj.delete()
    return tenent_detail(request)


def delete_rent_detail(request, ID):
    rent_detail_obj = Rent.objects.get(pk=ID)
    rent_detail_obj.delete()
    return rent_detail(request)

def add_home_detail(request):
    return render(request,'home_detail_modify.html', {'home_detail': 'NEW'})

def add_tenent_detail(request):
    home_detail_obj = Home.objects.all()
    return render(request, 'tenent_detail_modify.html', {'tenent_detail': 'NEW', 'home_object': home_detail_obj})

def add_rent_detail(request):
    tenent_detail_obj = Tenent.objects.all().select_related('tenent_home_id')    

    tenent_list = []
    for tenent in tenent_detail_obj:
        tenent_single_entry_list = [
        tenent.id,
        tenent.tenent_name,
        tenent.tenent_home_id.home_location,
        tenent.tenent_home_id.home_floor]
        tenent_list.append(tenent_single_entry_list)

    return render(request, 'rent_detail_modify.html', {'rent_detail': 'NEW', 'tenent_object': tenent_detail_obj})

def rent_next_page(request, page_count):
    return rent_detail(request, current_page=page_count + 1)


def rent_prev_page(request, page_count):
    if page_count > 1:
        return rent_detail(request, current_page=page_count - 1)
    else:
        return rent_detail(request)

@api_view(('GET',))
@renderer_classes((TemplateHTMLRenderer, JSONRenderer))
def search_rent_filiter(request):
    [...]
    search_keyword = request.GET['search_keyword']
    home_list1 = Home.objects.filter(home_name__contains=search_keyword).values()
    home_list2 = Home.objects.filter(home_location__contains=search_keyword).values()
    home_list3 = Home.objects.filter(home_address__contains=search_keyword).values()
    home_list4 = Home.objects.filter(home_floor__contains=search_keyword).values()

    #Entry.objects.get(title__regex=r"^(An?|The) +")    
    home_list = []
    for home in home_list1:
        if home not in home_list:
            home_list.append(home)
    for home in home_list2:
        if home not in home_list:
            home_list.append(home)
    for home in home_list3:
        if home not in home_list:
            home_list.append(home)
    for home in home_list4:
        if home not in home_list:
            home_list.append(home)

    rent_list = []
    for home in home_list:
            result = Rent.objects.filter(rent_tenent_id=int(home["id"])).order_by('-id')[:10]
            rent_list.append(result)

    rent = []
    for resultList in rent_list:
        for result in resultList:
            list = [result.id,
            result.rent_month_year,
            result.rent_recived_date,
            result.rent_tenent_id.tenent_home_id.home_name,
            result.rent_tenent_id.tenent_name,
            result.rent_amount]
            rent.append(list)
        
    data = {'rent_list': rent}
    return Response(data, status=status.HTTP_200_OK)


def update_home_detail(request):
    if len(request.POST['home_id'])<=0:

        home_Obj = Home(
            home_name=request.POST['home_name'],
            home_location=request.POST['home_location'],
            home_rent=int(request.POST['home_rent']),
            home_floor=request.POST['home_floor'],
            home_painting_money=int(request.POST['home_painting_money']),
            home_address=request.POST['home_address'])

    else:

        home_Obj = Home.objects.get(id=request.POST['home_id'])  # object to update
        home_Obj.home_name = request.POST['home_name']
        home_Obj.home_location = request.POST['home_location']
        home_Obj.home_rent = int(request.POST['home_rent'])
        home_Obj.home_floor = request.POST['home_floor']
        home_Obj.home_painting_money = int(request.POST['home_painting_money'])
        home_Obj.home_address = request.POST['home_address']

    home_Obj.save()
    return home_detail(request)


def update_tenent_detail(request):

    if len(request.POST['tenent_id'])<=0:

        tenent_Obj = Tenent(
            tenent_name=request.POST['tenent_name'],
            tenent_start_date=getDate_from_string(request.POST['tenent_start_date']),
            tenent_end_date=getDate_from_string(request.POST['tenent_end_date']),
            tenent_home_id=Home.objects.get(id=request.POST['tenent_home_id']),
            tenent_advance=request.POST['tenent_advance'],
            tenent_note=request.POST['tenent_note'])

    else:

        tenent_Obj = Tenent.objects.get(id=request.POST['tenent_id'])  # object to update
        tenent_Obj.tenent_name = request.POST['tenent_name']
        tenent_Obj.tenent_start_date = getDate_from_string(request.POST['tenent_start_date'])
        tenent_Obj.tenent_end_date = getDate_from_string(request.POST['tenent_end_date'])
        tenent_Obj.tenent_home_id = Home.objects.get(id=request.POST['tenent_home_id'])
        tenent_Obj.tenent_advance = int(request.POST['tenent_advance'])
        tenent_Obj.tenent_note = request.POST['tenent_note']

    tenent_Obj.save()
    return tenent_detail(request)


def update_rent_detail(request):

    if len(request.POST['rent_id'])<=0:

        rent_Obj = Rent(
            rent_tenent_id=Tenent.objects.get(id=request.POST['rent_tenent_id']),
            rent_month_year=getDate_from_string(request.POST['rent_month_year']),
            rent_recived_date=getDate_from_string(request.POST['rent_recived_date']),
            rent_amount=int(request.POST['rent_amount'])
            )

    else:

        rent_Obj = Rent.objects.get(id=request.POST['rent_id'])  # object to update
        rent_Obj.rent_tenent_id = Tenent.objects.get(id=request.POST['rent_tenent_id'])
        rent_Obj.rent_month_year = getDate_from_string(request.POST['rent_month_year'])
        rent_Obj.rent_recived_date = getDate_from_string(request.POST['rent_recived_date'])
        rent_Obj.rent_amount = request.POST['rent_amount']


    rent_Obj.save()
    return rent_detail(request)


def getDate_from_string(stringDate):
    mystringDate = str(stringDate).split("-")
    return datetime.date(int(mystringDate[0]), int(mystringDate[1]), int(mystringDate[2]))