from django.shortcuts import render
from .models import Employee, Vendor, MRMmodels, AI_ML
from django.http import JsonResponse
from django.http import HttpResponseRedirect
from django.contrib import messages 
from django.contrib.auth import authenticate, login, logout 
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control

# Create your views here.

#######################################################################################################
########################## LOGIN/LOGOUT/SIGN UP #######################################################
#######################################################################################################
 
def sign_up(request):
    return render(request, "home.html",{})

def Login(request):
    if request.user.is_authenticated:
        return render(request, "home.html")
    else:
        messages.info(request, "Please login to access this page")
        return HttpResponseRedirect("/")

def LoginUser(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user != None:
            login(request, user)
            return HttpResponseRedirect("/") # /backend ??
        else:
            messages.error(request, "Enter your data correctly")
            return HttpResponseRedirect("/")


def LogoutUser(request):
    logout(request)
    request.user = None
    return HttpResponseRedirect("/")

#######################################################################################################
########################## EMPLOYEES ####################################################################
#######################################################################################################


def home(request):
    Employees = Employee.objects.all().order_by('-created_at')
    return render(request, "home.html",{"Employees":Employees})

""" #JSON
def employee_json(request):
    Employees = Employee.objects.all()
    data = [Employee.get_data() for Employee in Employees]
    response = {'data':data}
    return JsonResponse(response) """

# add employee
def add_employee(request):
    if request.method == "POST":
        if request.POST.get('name')\
            and request.POST.get('email')\
            and request.POST.get('occupation')\
            and request.POST.get('salary')\
            and request.POST.get('gender')\
            or request.POST.get('notes'):
            employee = Employee()
            employee.name = request.POST.get('name')
            employee.email = request.POST.get('email')
            employee.occupation = request.POST.get('occupation')
            employee.salary = request.POST.get('salary')
            employee.gender = request.POST.get('gender')
            employee.notes = request.POST.get('notes')
            employee.save()
            messages.success(request, "Employee added Successfully")
            return  HttpResponseRedirect("/")
    else:
        return render(request, "add_employee.html")

    
#path to view employee data individually
def employee(request, employee_id):
    employee = Employee.objects.get(id=employee_id)
    if employee != None:
        return render(request, "edit.html", {"employee":employee})

    
#path to edit employee
def edit_employee(request):
    if request.method == "POST":
        employee = Employee.objects.get(id=request.POST.get('id'))
        if employee != None:
            employee.name = request.POST.get('name')
            employee.email = request.POST.get('email')
            employee.occupation = request.POST.get('occupation')
            employee.salary = request.POST.get('salary')
            employee.gender = request.POST.get('gender')
            employee.notes = request.POST.get('notes')
            employee.save()
            messages.success(request, "Employee updated Successfully")
            return  HttpResponseRedirect("/")
 
    
#path to delete employee
def delete_employee(request, employee_id):
    employee = Employee.objects.get(id=employee_id)
    employee.delete()
    messages.success(request, "Employee deleted successfully")
    return HttpResponseRedirect("/")

#######################################################################################################
########################## VENDORS ####################################################################
#######################################################################################################

@login_required(login_url='/vendors')
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def vendors(request):
    vendors = Vendor.objects.all()
    return render(request, "vendors.html",{"vendors":vendors})

# add vendor
def add_vendor(request):
    if request.method == "POST":
        if request.POST.get('name')\
            and request.POST.get('email')\
            or request.POST.get('industry'):
            vendor = Vendor()
            vendor.name = request.POST.get('name')
            vendor.email = request.POST.get('email')
            vendor.industry = request.POST.get('industry')
            vendor.save()
            messages.success(request, "Vendor added Successfully")
            return  HttpResponseRedirect("/")
    else:
        return render(request, "vendors.html")

#path to edit vendor
def edit_vendor(request):
    if request.method == "POST":
        vendor = Vendor.objects.get(id=request.POST.get('id'))
        if vendor != None:
            vendor.name = request.POST.get('name')
            vendor.email = request.POST.get('email')
            vendor.industry = request.POST.get('industry')
            vendor.save()
            messages.success(request, "Vendor updated Successfully")
            return  HttpResponseRedirect("/")
  
#path to delete vendor
def delete_vendor(request, vendor_id):
    vendor = Vendor.objects.get(id=vendor_id)
    vendor.delete()
    messages.success(request, "Vendor deleted successfully")
    return HttpResponseRedirect("/")

#######################################################################################################
########################## MRM MODELS ####################################################################
#######################################################################################################

@login_required(login_url='/mrm_models')
def mrm_models(request):
    mrm_models = MRMmodels.objects.all()
    return render(request, "mrm_models.html", {"mrm_models":mrm_models})

def add_mrm_model(request):
    if request.method == "POST":
        if request.POST.get('name')\
            and request.POST.get('rating')\
            or request.POST.get('lob'):
            mrm_model = MRMmodels()
            mrm_model.name = request.POST.get('name')
            mrm_model.rating = request.POST.get('rating')
            mrm_model.lob = request.POST.get('lob')
            mrm_model.save()
            messages.success(request, "MRM MOdel  added Successfully")
            return  HttpResponseRedirect("/")
    else:
        return render(request, "add_mrm_model.html")
   
#path to edit MRM Model
def edit_mrm_model(request):
    if request.method == "POST":
        mrm_model = MRMmodels.objects.get(id=request.POST.get('id'))
        if mrm_model != None:
            mrm_model.name = request.POST.get('name')
            mrm_model.rating = request.POST.get('rating')
            mrm_model.lob = request.POST.get('lob')
            mrm_model.save()
            messages.success(request, "MRM Model updated Successfully")
            return  HttpResponseRedirect("/")
  
#path to delete MRM Model
def delete_mrm_model(request, mrm_model_id):
    mrm_model = MRMmodels.objects.get(id=mrm_model_id)
    mrm_model.delete()
    messages.success(request, "MRM Model deleted successfully")
    return HttpResponseRedirect("/")

#######################################################################################################
########################## AI-ML ####################################################################
#######################################################################################################

def ai_ml(request):
    ai_ml_list = AI_ML.objects.all()
    return render(request, "AI_ML.html",{"ai_ml_list":ai_ml_list})

def add_ai_ml(request):
    if request.method == "POST":
        if request.POST.get('name')\
            and request.POST.get('language')\
            or request.POST.get('developer'):
            ai_ml = AI_ML()
            ai_ml.name = request.POST.get('name')
            ai_ml.language = request.POST.get('language')
            ai_ml.developer = request.POST.get('developer')
            ai_ml.save()
            messages.success(request, "AI ML added Successfully")
            return  HttpResponseRedirect("/")
    else:
        return render(request, "add_ai_ml.html")

#path to edit AI ML
def edit_ai_ml(request):
    if request.method == "POST":
        ai_ml = AI_ML.objects.get(id=request.POST.get('id'))
        if ai_ml != None:
            ai_ml.name = request.POST.get('name')
            ai_ml.language = request.POST.get('language')
            ai_ml.developer = request.POST.get('developer')
            ai_ml.save()
            messages.success(request, "AI ML updated Successfully")
            return  HttpResponseRedirect("/")
  
#path to delete MRM Model
def delete_ai_ml(request, ai_ml_id):
    ai_ml = AI_ML.objects.get(id=ai_ml_id)
    ai_ml.delete()
    messages.success(request, "AI ML deleted successfully")
    return HttpResponseRedirect("/")


