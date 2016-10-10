from django.shortcuts import render,render_to_response
# Create your views here.
import os
from myweb.settings import BASE_DIR
from pub_form.form_upload import UploadFile
from django.http import HttpResponse

#For upload
def handle_upload(f):
    path = os.path.join(BASE_DIR, 'upload/').replace('\\', '/')
    filename=path+f.name
    with open(filename,'wb+') as desction:
        for chunk in f.chunks():
            desction.write(chunk)

def ipadd(request):
    mo='hello ip add pages'
  #upload things
    if request.method =="POST":
        uf = UploadFile(request.POST,request.FILES)
        if uf.is_valid():
            handle_upload(uf.cleaned_data['file'])
            return HttpResponse('successful!')
    else:
        uf = UploadFile()

    return render_to_response('ip/ipadd.html',locals())
