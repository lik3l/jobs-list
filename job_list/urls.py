"""job_list URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
# from django.contrib import admin
from django.urls import path
from core import views as core_views
from jobs import views as job_views

urlpatterns = [
    path('', core_views.index, name='index'),
    path('finish/<int:pk>/', core_views.finish_job, name='finish_job'),
    path('start/<int:pk>/', core_views.start_job, name='start_job'),
    path('', core_views.index, name='index'),
    path('login/', core_views.login_view, name='login'),
    path('logout/', core_views.logout_view, name='logout'),
    path('add-job/', core_views.create_job, name='add_job'),
    path('add-price/<int:pk>', job_views.add_company_price, name='add_price'),
    path('calculate-price/', job_views.calculate_price, name='calculate_price'),
    path('companies/', job_views.company_list, name='company_list'),
    path('companies/<int:pk>/', job_views.company_detail, name='company_detail'),
    path('companies/add', job_views.add_company, name='company_add'),
    path('companies/delete/<int:pk>/', job_views.company_delete, name='company_delete'),
    path('materials/', job_views.material_list, name='material_list'),
    path('materials/<int:pk>/', job_views.material_detail, name='material_detail'),
    path('materials/add', job_views.add_material, name='material_add'),
    path('materials/delete/<int:pk>/', job_views.material_delete, name='material_delete'),
]
