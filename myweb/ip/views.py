from django.shortcuts import render,render_to_response
# Create your views here.
import os
from myweb.settings import BASE_DIR
from django.http import HttpResponse
from pub_form.form_ipadd import ipForm
from . import models

#For upload
def handle_upload(f):
    path = os.path.join(BASE_DIR, 'upload/').replace('\\', '/')
    filename=path+f.name
    with open(filename,'wb+') as desction:
        for chunk in f.chunks():
            desction.write(chunk)



#For ipaddtable

def ipadd(request):
    if request.method =="POST":
        uf = ipForm(request.POST,request.FILES)
        if uf.is_valid():
            ip=uf.cleaned_data['ip']
            user=uf.cleaned_data['user']
            password=uf.cleaned_data['password']

            table=models.iptable()
            table.ip=ip
            table.user=user
            table.password=password
            table.save()

            handle_upload(uf.cleaned_data['file'])
            return HttpResponse('successful!')
    else:
        uf = ipForm()
    return render_to_response('ip/ipadd.html',locals())
