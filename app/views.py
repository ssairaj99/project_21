from django.shortcuts import render
from app.models import *
# Create your views here.

def insert_Dept(request):
    dto=input()
    dn=input()
    lc=input()
    NTO=Dept.objects.get_or_create(deptno=dto,dname=dn,loc=lc)[0]
    NTO.save()
    return HttpResponse("Topic is created")
