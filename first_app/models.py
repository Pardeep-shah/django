from django.db import models
from django.contrib.auth.models import User
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
    

    
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)  # Optional: for guest carts
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Cart ID: {self.id} - User: {self.user if self.user else 'Guest'}"

    def get_total(self):
        return sum(item.get_subtotal() for item in self.cartitem_set.all())
    

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    
    product = models.ForeignKey(Category_Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} x {self.product.product_name}"

    def get_subtotal(self):
        return self.quantity * self.product.selling_price
    


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    full_name = models.CharField(max_length=255)
    address = models.TextField()
    city = models.CharField(max_length=100)
    # state = models.CharField(max_length=100)
    pincode = models.CharField(max_length=10)
    country = models.CharField(max_length=100, default='India')
    payment_method = models.CharField(max_length=20, choices=[
        ('COD', 'Cash on Delivery'),
        ('Card', 'Credit/Debit Card'),
        ('UPI', 'UPI')
    ])
    
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.id} by {self.user.username}"
    

    
class OrderItem(models.Model):
    order = models.ForeignKey('Order', on_delete=models.CASCADE, related_name='items')  
    product = models.ForeignKey(Category_Product, on_delete=models.SET_NULL, null=True)
    quantity = models.PositiveIntegerField()
    price_at_purchase = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.quantity} x {self.product.product_name} in Order #{self.order.id}"

    def get_subtotal(self):
        return self.quantity * self.price_at_purchase







class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Category_Product, on_delete=models.CASCADE)
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'product')  # Prevent duplicates

    def __str__(self):
        return f"{self.user.username}'s Wishlist Item: {self.product.product_name}"


