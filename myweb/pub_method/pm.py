import os
from myweb.settings import BASE_DIR
import MySQLdb
from django.http import HttpResponse



def handle_upload(f):
    path = os.path.join(BASE_DIR, 'upload/').replace('\\', '/')
    filename=path+f.name
    with open(filename,'wb+') as desction:
        for chunk in f.chunks():
            desction.write(chunk)


    open_file(filename)


def open_file(filename):
  iplist=[]
  userlist=[]
  passwordlist=[]
  try:
    if str(filename).endswith('.txt'):
        with open(filename) as f:

            data =f.readlines()
            for line in data:
                line=line.replace('\n','').split()
                iplist.append(line[0])
                userlist.append(line[1])
                passwordlist.append(line[2])

            val=[]
            for ip,user,password in zip(iplist,userlist,passwordlist):
                val.append((ip,user,password))

            mysql_insert(val)
    else:
        print ("The file is not txt file")


  except Exception,ex:
        print ("Sorry,some error!")



def mysql_insert(val):
  try:

       conn = MySQLdb.connect(host='localhost', user='root', passwd='123', port=3306, db='mmot')
       cur = conn.cursor()
       cur.executemany("insert into ip_iptable(ip,user,password) values(%s,%s,%s)", val)
       conn.commit()
       cur.close()
       conn.close()

  except MySQLdb.Error, e:
          print ('Some error!')
