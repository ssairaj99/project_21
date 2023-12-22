from django.db import models

# Create your models here.

class Dept(models.Model):
    deptno=models.IntegerField(primary_key=True)
    dname=models.CharField(max_length=100)
    loc=models.CharField(max_length=100)

    def _str_(self):
        return self.dname
    
    
     
class Emp(models.Model):
    empno=models.IntegerField(primary_key=True)
    ename=models.CharField(max_length=100)
    job=models.CharField(max_length=100)
    mgr=models.IntegerField()
    hiredate=models.DateField()
    sal=models.IntegerField()
    comm=models.IntegerField()
    deptno=models.ForeignKey(Dept,on_delete=models.CASCADE)

    def _int_(self):
        return self.deptno