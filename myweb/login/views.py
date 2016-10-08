from django.shortcuts import render,render_to_response
from login import models
from django.http import HttpResponseRedirect
from pub_form.form_login import UserForm
from django.core.paginator import Paginator


# Create your views here.

def index(request):
   
    current_page=request.GET.get("page",1)

    mo = models.Notice.objects.all()
    pages=Paginator(mo,6)
    mo=pages.page(current_page)

    if request.method=='POST':
        uf =UserForm(request.POST)
        if uf.is_vaild():
            username=uf.cleaned_data['username']
            password=uf.cleaned_data['password']
            return HttpResponseRedirect('base.html')
    else:
        uf = UserForm()
    return render_to_response('login.html',locals())


def main(request):
    hh = 'hello there'
    return render_to_response('base.html',locals())    