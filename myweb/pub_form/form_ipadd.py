from django import forms
from django.forms import ModelForm
from ip.models import iptable

#ipadd

class ipForm(ModelForm):

    class Meta:
        model = iptable
        fields = '__all__'

        labels={
            'ip':'IpAddress'
        }
