from dataclasses import fields
from django.contrib.auth.models import User
from django import forms
from .models import *


class ActiveIngredientForm(forms.ModelForm):
    class Meta:
        model = ActiveIngredient
        fields = "__all__"

# class UserRegisterForm(forms.Form):
#     last_name = forms.CharField(max_length=20)
#     first_name = forms.CharField(max_length=20)
#     birth_date = forms.DateField()



class UserRegisterModelForm(forms.ModelForm):

    confirm = forms.CharField(widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['last_name', 'first_name', 'username', 'email', 'password', 'confirm']
        widgets = {
            'password': forms.PasswordInput(),
        }

