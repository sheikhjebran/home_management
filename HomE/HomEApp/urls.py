from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('about.html', views.about, name="about"),
    path('contact.html', views.contact, name="contact"),
    path('services.html', views.services, name="services"),
    path('index.html', views.home, name="home"),
    path('login.html', views.login, name="login"),
    path('authenticate', views.get_authenticate, name="get_authenticate"),
    path('rent', views.rent_detail, name="rent_detail"),
    path('tenent', views.tenent_detail, name="tenent_detail"),
    path('home_detail', views.home_detail, name="home_detail"),
    path('search', views.search, name="search"),
    path('logout', views.logout, name="logout"),

    path('home_detail_modify/<int:ID>/',views.home_detail_modify, name="home_detail_modify"),
    path('add_home_detail',views.add_home_detail, name="add_home_detail"),
    path('update_home_detail', views.update_home_detail, name='update_home_detail'),
    path('Delete_home_detail/<int:ID>/',views.delete_home_detail, name="delete_home_detail"),

    path('tenent_detail_modify/<int:ID>/', views.tenent_detail_modify, name="tenent_detail_modify"),
    path('Delete_tenent_detail/<int:ID>/',views.delete_tenent_detail, name="delete_tenent_detail"),
    path('update_tenent_detail', views.update_tenent_detail, name='update_tenent_detail'),
    path('add_tenent_detail',views.add_tenent_detail, name="add_tenent_detail"),

    path('rent_detail_modify/<int:ID>/', views.rent_detail_modify, name="rent_detail_modify"),
    path('Delete_rent_detail/<int:ID>/',views.delete_rent_detail, name="delete_rent_detail"),
    path('update_rent_detail', views.update_rent_detail, name='update_rent_detail'),
    path('add_rent_detail',views.add_rent_detail, name="add_rent_detail"),

]
