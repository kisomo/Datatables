from django.contrib import admin

from django.contrib import admin
from django.contrib.auth.models import Group

from .models import Employee, Vendor, MRMmodels, AI_ML

#admin.site.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['id','name','email','occupation','salary','gender','notes','created_at']
    search_fields = ['name']
    list_filter = ['gender']
    list_per_page = 3

admin.site.register(Employee, EmployeeAdmin)

admin.site.register(Vendor)

admin.site.register(MRMmodels)

admin.site.register(AI_ML)



