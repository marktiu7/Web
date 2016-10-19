from django.shortcuts import render,render_to_response


def hello(request):
    return render_to_response('iptables/iptables.html',locals())

# Create your views here.
