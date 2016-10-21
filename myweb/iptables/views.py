from django.shortcuts import render,render_to_response
from ip.models import iptable
import paramiko
from django.http import HttpResponse



def show(r):

    ssh=paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect('192.168.49.137',22,'root','123456')
    stdin,stdout,stderr =ssh.exec_command('iptables -nL')
    b=stdout.readlines()
    return b


def tablesshow(request):
    drop=request.GET['drop']
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(drop, 22, 'root', '123456' )
    stdin, stdout, stderr = ssh.exec_command('iptables -nL')
    b = stdout.readlines()
    return HttpResponse(b)


def iptablesshow(request):
    downlist=iptable.objects.values('ip').distinct()
    b=show(request)
    return render_to_response('iptables/iptables.html',{'downlist':downlist,'b':b,})


