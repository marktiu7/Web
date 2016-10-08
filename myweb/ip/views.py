from django.shortcuts import render,render_to_response
# Create your views here.

def ipadd(request):
    mo='hello ip add pages'
    return render_to_response('ip/ipadd.html',locals())
