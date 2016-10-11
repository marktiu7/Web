from django import forms
from django.forms import ModelForm
from login.models import *

#login

class UserForm(ModelForm):

    class Meta:
        model = login
        fields = '__all__'

        labels ={
            'username':'yonghuming',
            'password':'mima',
        }
        
        widgets ={
            'password':forms.PasswordInput,
        }

        error_messages ={
            'username':{
                'invalid':'haha'
            }
        }