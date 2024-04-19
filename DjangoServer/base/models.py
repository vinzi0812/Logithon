from django.db import models

# Create your models here.
class Managers(models.Model):
    ManagerID = models.AutoField(primary_key=True)
    
    
class Employees(models.Model):
    EmployeeID = models.AutoField(primary_key= True)
    Manager = models.CharField(max_length= 500)
    EmployeeName = models.CharField(max_length=500)
    PhotoFileName = models.CharField(max_length =500)
    