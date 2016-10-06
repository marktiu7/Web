from django.shortcuts import render,render_to_response
from login import models

# Create your views here.

def index(request):
    mo = models.Notice.objects.all()

    return render_to_response('login.html',locals())