from django.db import models

# Create your models here.

# here we have to define structure of any table in my dtabase 

class Student(models.Model):
    f_name = models.CharField(max_length=100)
    l_name = models.CharField(max_length=100)
    registration_id = models.CharField(max_length=100)


class Employee(models.Model):
    Emp_id= models.CharField(max_length=100)
    emp_first_name= models.CharField(max_length=100)
    emp_last_name= models.CharField(max_length=100)
    emp_city= models.CharField(max_length=100)
    salary= models.CharField(max_length=100)
    cmp_name= models.CharField(max_length=100)


class Category(models.Model):
    Category_name = models.CharField(max_length=100)
    Category_description = models.TextField(max_length=100)
    Category_image = models.ImageField(upload_to='Category_image')


    def __str__(self):
       return self.Category_name
    

    


   
class Category_Product(models.Model):
    product_category_name = models.ForeignKey(Category, on_delete=models.CASCADE)
    product_image = models.ImageField(upload_to='product_images')
    product_name = models.CharField(max_length=100)
    product_description = models.TextField(max_length=500)
    selling_price = models.DecimalField(max_digits=10, decimal_places=2)
    original_price = models.DecimalField(max_digits=10, decimal_places=2)
    product_quantity = models.IntegerField()

    def __str__(self):
        return self.product_name
    


