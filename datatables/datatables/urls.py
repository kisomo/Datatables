"""datatables URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from App import views 

urlpatterns = [
    # path to access the admin panel
    path('admin/', admin.site.urls),
    #path to render homepage
    path('',views.home, name="home"),
    # path to JSON response
    #path('json/',views.employee_json, name="employee-json"),
    
    #path to view employee data individually
    path('employee/<str:employee_id>',views.employee, name="employee"),
    #path to add employee
    path('add_employee',views.add_employee, name="add-employee"),
    #path to edit employee
    path('edit_employee',views.edit_employee, name="edit-employee"),
    #path to delete employee
    path('delete_employee/<str:employee_id>',views.delete_employee, name="delete_employee"),

    #vendors
    path('vendors',views.vendors, name="vendors"),
    #add vendor
    path('add_vendor',views.add_vendor, name="add-vendor"),
    # edit vendor
    path('edit_vendor',views.edit_vendor, name="edit-vendor"),
    #delete vendor
    path('delete_vendor/<str:vendor_id>',views.delete_vendor, name="delete-vendor"),

    #MRM models
    path('mrm_models',views.mrm_models, name="mrm_models"),
    # add MRM Model 
    path('add_mrm_model',views.add_mrm_model, name="add-mrm-model"),
    #edit MRM Model 
    path('edit_mrm_model',views.edit_mrm_model, name="edit-mrm-model"),
    # delete MRM Model 
    path('delete_mrm_model/<str:mrm_model_id>',views.delete_mrm_model, name="delete-mrm-model"),

    # AI ML 
    path('ai_ml',views.ai_ml, name="ai_ml"),
    # add AI ML 
    path('add_ai_ml',views.add_ai_ml, name="add_ai_ml"),
    # edit AI ML 
    path('edit_ai_ml',views.edit_ai_ml, name="edit_ai_ml"),
    # delete AI ML
    path('delete_ai_ml/<str:ai_ml_id>',views.delete_ai_ml, name="delete_ai_ml"),

    path('sign_up',views.sign_up, name="sign_up"),
    path('login/',views.Login, name="login"),
    path('login_user',views.LoginUser, name="login_user"),
    path('logout/',views.LogoutUser, name="logout"),

]


