from django.shortcuts import render,render_to_response
# Create your views here.
import os
from myweb.settings import BASE_DIR
from django.http import HttpResponse
from pub_form.form_ipadd import ipForm
from . import models
from pub_form.form_upload import UploadFile

#For upload
def handle_upload(f):
    path = os.path.join(BASE_DIR, 'upload/').replace('\\', '/')
    filename=path+f.name
    with open(filename,'wb+') as desction:
        for chunk in f.chunks():
            desction.write(chunk)


def upload(r):
    if r.method=="POST":
        upfile=UploadFile(r.POST,r.FILES)
        if upfile.is_valid():
          handle_upload(upfile.cleaned_data['file'])
          return HttpResponse('successful!')
    else:
        upfile=UploadFile()

    return upfile
#For ipaddtable


def ipaddtable(r):
    if r.method =="POST":
        uf = ipForm(r.POST)
        if uf.is_valid():
            ip=uf.cleaned_data['ip']
            user=uf.cleaned_data['user']
            password=uf.cleaned_data['password']

            table=models.iptable()
            table.ip=ip
            table.user=user
            table.password=password
            table.save()

            return HttpResponse('successful!')
    else:
        uf = ipForm()
    return uf


def ipadd(request):
    ipleft=ipaddtable(request)
    ipright=upload(request)
    return render_to_response('ip/ipadd.html',locals())
