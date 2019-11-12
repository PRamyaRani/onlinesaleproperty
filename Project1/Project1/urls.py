"""Project1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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

from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),
    path('user_login/',views.user_login,name="user_login"),
    path('addplot/',views.addplot,name="addplot"),
    path('editplot',views.editplot,name="editplot"),
    path('editplot_details/',views.editplot_details,name="editplot_details"),
    path('update_plot/',views.update_plot,name="update_plot"),
    path('viewplot',views.viewplot,name="viewplot"),
    path('view_plot_details/',views.view_plot_details,name="view_plot_details"),
    path('saveplot/',views.saveplot,name="saveplot"),
    path('addappartment/',views.addappartment,name="addappartment"),
    path('editappartment',views.editappartment,name="editappartment"),
    path('viewappartment',views.viewappartment,name="viewappartment"),
    path('saveappartment',views.saveappartment,name="saveappartment"),
    path('view_appart_details/',views.view_appart_details,name="view_appart_details"),
    path('edit_appart_details/',views.edit_appart_details,name="edit_appart_details"),
    path('update_appart/',views.update_appart,name="update_appart"),
    path('addemployee',views.addemployee,name="addemployee"),
    path('editemployee',views.editemployee,name="updateemployee"),
    path('deleteemployee',views.deleteemployee,name="deleteemployee"),
    path('delete_employee_details/',views.delete_employee_details,name="delete_employee_details"),
    path('saveemployee/',views.saveemployee,name="saveemployee"),
    path('view_employee_details/',views.view_employee_details,name="view_emloyee_details"),
    path('editemployee_details/',views.editemployee_details,name="editemployee_details"),
    path('update_employee/', views.update_employee, name="update_employee"),


]
