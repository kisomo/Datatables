
from django import forms 
from django.forms import ModelForm
from . models import Employee, Vendor, MRMmodels, AI_ML


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ("__all__")
        
       """  widgets = {
            'fname': forms.TextInput(attrs= {'class':'form-control'}),
            'lname': forms.TextInput(attrs= {'class':'form-control'}),
            'phone_number': forms.TextInput(attrs= {'class':'form-control'}),
            'doc': forms.Select(attrs= {'class':'form-select'}),
            'manager': forms.Select(attrs= {'class':'form-select'}),
        } """
        
class VendorForm(forms.ModelForm):
    class Meta:
        model = Vendor
        fields = ("__all__")


class MRMmodelsForm(forms.ModelForm):
    class Meta:
        model = MRMmodels
        fields = ("__all__")

class AI_MLForm(forms.ModelForm):
    class Meta:
        model = AI_ML
        fields = ("__all__")

