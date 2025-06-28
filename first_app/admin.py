from django.contrib import admin
from .models import *

# from .models import Student
# Register your models here.

admin.site.register(Student)

admin.site.register(Employee)

admin.site.register(Category)
admin.site.register(Category_Product)



