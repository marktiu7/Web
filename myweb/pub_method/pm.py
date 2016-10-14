import os
from myweb.settings import BASE_DIR
import MySQLdb



def handle_upload(f):
    path = os.path.join(BASE_DIR, 'upload/').replace('\\', '/')
    filename=path+f.name
    with open(filename,'wb+') as desction:
        for chunk in f.chunks():
            desction.write(chunk)
            print desction

def open_file(filename):
  iplist=[]
  userlist=[]
  passwordlist=[]
  try:
    if str(filename).endswith('.txt'):
        with open(filename) as f:
            print f
            print type(f)
            data =f.readlines()
            for line in data:
                line=line.replace('\n','').split()
                iplist.append(line[0])
                userlist.append(line[1])
                passwordlist.append(line[2])
            print iplist
            print userlist
            print passwordlist
            mysql_insert(iplist,userlist,passwordlist)
    else:
        print ("The file is not txt file")


  except Exception,ex:
        print ("Sorry,some error!")



def mysql_insert(iplist,userlist,passwordlist):

    try:
       conn=MySQLdb.connect(host='localhost',user='root',passwd='123',port=3306)
       cur =conn.cursor()
       cur.execture('create database if not exists python')
       conn.select_db('mmot')
       for ip,user,password in zip(iplist,userlist,passwordlist):
           cur.execture('insert into ip_iptable(ip,user,password) values(%s,%s,%s) ' %(ip,user,password))
       cur.close()
       conn.close()
    except MySQLdb.Error,e:
        print ('Some error!')