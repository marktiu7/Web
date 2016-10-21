from django import forms
from ip.models import iptable
from django.forms import ModelForm

class iplist(ModelForm):
    class Meta:
        model = iptable
        fields = ['ip']
        widgets ={
            'ip':forms.ChoiceField,
        }
