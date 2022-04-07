from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('about.html', views.about, name="about"),
    path('contact.html', views.contact, name="contact"),
    path('services.html', views.services, name="services"),
    path('index.html', views.home, name="home"),
    path('login.html', views.login, name="login"),
    path('authenticate', views.authenticate, name="authenticate"),
    path('rent', views.rent_detail, name="rent_detail"),
    path('tenent', views.tenent_detail, name="tenent_detail"),
    path('home_detail', views.home_detail, name="home_detail"),
]
