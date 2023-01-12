from django.db import models
from django.contrib.auth.models import User
from datetime import date
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.

class Employee(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField('Name', max_length=200)
    email = models.EmailField('Email', max_length=200)
    occupation = models.CharField('Occupation', max_length=25)
    salary = models.IntegerField()
    gender = models.CharField('Gender', max_length=25)
    notes = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    #JSON 
    def get_data(self):
        return {
            'id':self.id,
            'name':self.name,
            'email':self.email,
            'occupation':self.occupation,
            'salary':self.salary,
            'gender':self.gender,
        }

class Vendor(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField('Name', max_length=200)
    email = models.EmailField('Email', max_length=200)
    industry = models.CharField('Industry', max_length=25)
    """ school = models.CharField('School', max_length=25)
    address = models.CharField('Address', max_length=25)
    city = models.CharField('City', max_length=25)
    town = models.CharField('Town', max_length=25)
    zipcode = models.CharField('Zip Code', max_length=25)
    phone = models.CharField('Phone', max_length=25)
    tenor = models.CharField('Tenor', max_length=25)
    revenue = models.CharField('Revenue', max_length=25)
    assets = models.CharField('Assets', max_length=25) """
    
    def __str__(self):
        return self.name 
        
class MRMmodels(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField('Name', max_length=200)
    rating = models.EmailField('Rating', max_length=200)
    lob = models.CharField('LOB', max_length=25)
    
    def __str__(self):
        return self.name 
        
class AI_ML(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField('Name', max_length=200)
    language = models.EmailField('Language', max_length=200)
    developer = models.CharField('Developer', max_length=25)
    
    def __str__(self):
        return self.name 
        

