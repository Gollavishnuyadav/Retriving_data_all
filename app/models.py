from django.db import models

# Create your models here.
class Emp(models.Model):
    Empno=models.IntegerField()
    Ename=models.CharField(max_length=100)
    Job=models.CharField(max_length=100)
    Mgr=models.IntegerField()
    Hiredate=models.DateField()
    Sal=models.IntegerField()
    Comm=models.IntegerField()
    Deptno=models.IntegerField()
    Ehttp=models.URLField()


    def __str__(self):
        return str(self.Empno)
class Dept(models.Model):
    Empno=models.ForeignKey(Emp,on_delete=models.CASCADE)
    Dname=models.CharField(max_length=100)
    Dloc=models.CharField(max_length=100)


    def __str__(self):
        return str(self.Dname)

