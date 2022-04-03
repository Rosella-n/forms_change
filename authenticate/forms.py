from pickle import FALSE
from django import forms
from django.core.exceptions import ValidationError
from django.forms import ModelForm
from authenticate. models import (User,State,Local_Government,\
Department,Country,User_Info)
import datetime
from django.contrib.auth.password_validation import validate_password




class SignUpForm(forms.Form):
    
    id_numb = forms.CharField( widget=forms.TextInput(attrs={'class': 
    'form-control','placeholder': 'ID Number',}))
    id_numb.label=''
    id_numb.required
    
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter Password',}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm Password',}))
      
    def clean_id_numb(self):
        id_numb = self.cleaned_data['id_numb']        
        r = User.objects.filter(id_numb=id_numb)
        
        if r.count():
            raise  ValidationError("ID Number {} already exists".format(id_numb))
        return id_numb
 
 
    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        user = self.cleaned_data.get('id_numb')
       
        validate_password(password1, user=user)
 
        if password1 and password2 and password1 != password2:
            raise ValidationError("Password don't match")
 
        return password2

   
    def save(self, commit=True):
        user = User.objects.create_user(
            # self.cleaned_data['email'],
            
            self.cleaned_data['id_numb'],
            self.cleaned_data['password1'],
            
        )
        return user


class LoginForm(forms.Form):
    id_numb = forms.CharField( widget=forms.TextInput(attrs={'class': 
    'form-control','placeholder': 'ID Number',}))
    id_numb.label=''
    # id_numb.required
    
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter Password',}))
    password.label='Password:'
