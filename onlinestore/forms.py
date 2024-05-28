from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Product,Category


class UserCreate(UserCreationForm):
    class Meta:
        model=User
        fields=['username','first_name','last_name','email','password1','password2']
        widgets={
            'username':forms.TextInput(attrs={'placeholder':'Username'}),
            'first_name':forms.TextInput(attrs={'placeholder':'First Name'}),
            'last_name':forms.TextInput(attrs={'placeholder':'Last Name'}),
            'email':forms.TextInput(attrs={'placeholder':'Email Address'}),
           
        }





class ProductForm(ModelForm):
    class Meta:
        model=Product
        fields=['name','price','des','ingredient','category','image']
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control','placeholder':'Product Name'}),
            'price':forms.TextInput(attrs={'class':'form-control','placeholder':'Price'}),
            'des':forms.TextInput(attrs={'class':'form-control','placeholder':'des'}),
            'ingredient':forms.TextInput(attrs={'class':'form-control','placeholder':'Ingredient'}),
           
            'image':forms.FileInput(attrs={'class':'form-control'})
        }

class CateForm(ModelForm):
    class Meta:
        model=Category
        fields=['name']
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control','placeholder':'Category Name'}),
        } 