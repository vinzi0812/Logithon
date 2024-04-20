from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import UserManager 

EMPLOYEE = 'Employee'
MANAGER = 'Manager'
# Create your models here.
class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=500)
    last_name = models.CharField(max_length=500)
    isManager = models.BooleanField(default=False)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'email']
    objects = UserManager()
    
    def __str__(self) -> str:
        return self.username
    
class Route(models.Model):
    source = models.CharField(max_length=500)
    destination = models.CharField(max_length=500)
    cost = models.IntegerField()
    carbon_emission = models.IntegerField()
    duration = models.IntegerField()
    mode_of_transport = models.CharField(max_length=500)
    places = models.CharField(max_length=500)
    manager = models.CharField(max_length=500, default="None")
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.source + " to " + self.destination