from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import HttpResponseRedirect,render_to_response,redirect
from django.db import connection
def index(request):
    return render(request,'index.html')
def login(request):
    return render(request,'login.html')
def regaction(request):
    cursor=connection.cursor()
    uname=request.GET['uname']
    passw=request.GET['password']
    passwd=request.GET['cpass']
    ut='person'
    sql="insert into register(uname,upass,cpass,utype)values('%s','%s','%s','%s')"%(uname,passw,passwd,ut)
    cursor.execute(sql)
    return render(request,'register.html')

def register(request):
    return render(request,'register.html')
def logaction(request):
    cursor=connection.cursor()
    uname=request.GET['uname']
    passw=request.GET['password']
    sql="select * from register where uname='%s' and upass='%s' "%(uname,passw)
    cursor.execute(sql)
    #datas
    if(cursor.rowcount)>0:
        dts=cursor.fetchall()
        for row in dts:
            request.session['rid']=row[0]
            request.session['uname']=row[1]
            request.session['upass']=row[2]
            request.session['utype']=row[4]
            if(request.session['utype']=='person'):
                request.session['rid']=row[0]
                return render(request,'welcome.html')
    else:
        message="<script>alert('login credential invalid');window.location='/register/';</script>"
        return HttpResponse(message)
def welcome(request):
    return render(request,'welcome.html')
def pinformation(request):
    return render(request,'pinformation.html')
def paction(request):
    cursor=connection.cursor()
    n=request.GET['t1']
    d=request.GET['t2']
    a=request.GET['t3']
    g=request.GET['t4']
    p=request.GET['t5']
    e=request.GET['t6']
    addr=request.GET['t11']
    dp=request.GET['t7']
    c=request.GET['t8']
    pr=request.GET['t9']
    m=request.GET['t10']
    sql="insert into pinformation(name,dob,age,gen,phno,email,addr,dept,course,purpose,material)values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"%(n,d,a,g,p,e,addr,dp,c,pr,m)
    cursor.execute(sql)
    message="<script>alert('Successfully Completed');window.location='/welcome/';</script>"
    return HttpResponse(message)

