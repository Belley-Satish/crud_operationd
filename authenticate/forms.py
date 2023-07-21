from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *

class UserRegisterForm(forms.Form, UserCreationForm):
   email= forms.EmailField(required=False)
   mobile=forms.IntegerField()

class loginform(forms.Form):
   username=forms.CharField(max_length=50, required=False)
   password=forms.CharField( max_length=50, required=False)

class to_do_list_form(forms.ModelForm):
   class Meta:
      model= to_do_list
      fields='__all__'
# class update_form(forms.ModelForm):
#    class Meta:
#       model=to_do_list
#       fields='__all__'

