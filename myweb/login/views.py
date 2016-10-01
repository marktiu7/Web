from django.shortcuts import render,render_to_response

# Create your views here.

def index(request):
    mo='hello there'
    return render_to_response('login.html',locals())