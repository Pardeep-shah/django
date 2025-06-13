from django.db import models

# Create your models here.

# here we have to define structure of any table in my dtabase 

class Student(models.Model):
    f_name = models.CharField(max_length=100)
    l_name = models.CharField(max_length=100)
    registration_id = models.CharField(max_length=100)



