"""amazon URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='Home Page'),
    path('about-us',views.about,name='About us Page'),
    path('services-page',views.service,name='Services Page'),
    path('admin-login',views.admin_login,name='Admin Login Page'),
    path('contact-us',views.contact,name='Contact Us Page'),
    path('admin-check',views.admincheck,name='Admin Login Check Page'),
    path('error-page',views.error,name='Error Page'),
    path('add-employee',views.addemployee,name='Add Employee Page'),
    path('reg-success',views.regsuccess,name='Admin Reg Success Page'),
    path('show-employee/',views.showemployee,name='Admin Show Employee'),
    path('single-record/<int:empid>/',views.showsinglerecord,name='Admin Show Single Record'),
    path('update-employee/<int:empid>/',views.updateemployee,name='Admin Update Employee'),
    path('delete-employee/<int:empid>/', views.deleteemployee, name='Admin Delete Employee')

]
