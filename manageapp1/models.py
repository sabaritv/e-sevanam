from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class Login(AbstractUser):
    is_govt = models.BooleanField(default=False)
    is_user = models.BooleanField(default=False)


class Department(models.Model):
    name= models.CharField(max_length=200)
    place= models.CharField(max_length=200)
    contact_number= models.CharField(max_length=100)
    email= models.EmailField()

    def __str__(self):
        return self.name



class Goverment(models.Model):
    user= models.OneToOneField(Login,on_delete=models.CASCADE,related_name='govt')
    name= models.CharField(max_length=100)
    contact_number=models.CharField(max_length=100)
    email =models.EmailField()
    address= models.TextField(max_length=200)
    department= models.ForeignKey(Department, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name


