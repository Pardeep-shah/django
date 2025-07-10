from django.shortcuts import render,redirect,get_object_or_404
from .models import Student
from .models import *
from django.contrib import messages
from django.views.decorators.http import require_POST
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Create your views here.


# REGISTER VIEW
def register_view(request):
    if request.method == 'POST':

        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken")
            return redirect('register')

        user = User.objects.create_user(
            username=username,
            password=password,
            first_name=first_name,
            last_name=last_name
        )
        messages.success(request, "Registration successful. Please login.")
        return redirect('login')

    return render(request, 'register.html')


# LOGIN VIEW
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        

        if user is not None:
            login(request, user)
            messages.success(request, "Login successful!")
            return redirect('home')  # Change to your desired homepage
        else:
            messages.error(request, "Invalid username or password")
            return redirect('login')

    return render(request, 'login.html')


# LOGOUT VIEW (optional)
def logout_view(request):
    logout(request)
    messages.success(request, "Logged out successfully.")
    return redirect('login')



def about_fxn(request):
    return render(request, 'about_us.html')


def contact_view(request):
    return render (request,'contact.html')

# fxn for home page view
def homePage_view(request):
    return render(request, 'home.html')

# fxn for contact_us page view
def contact_us_view(request):
    return render(request, 'contact_us.html')

# fxn for about_us page view
def about_us_view(request):
    return render(request, 'about_us.html')

# fxn for privacy_policy page view 
def privacy_policy_view(request):
    return render(request,'privacy_policy.html')

# fxn for our_vision page view
def our_vision_view(request):
    return render(request,'our_vision.html')

# fxn for our_mission page view
def our_mission_view(request):
    return render(request,'our_mission.html')

# fxn for return_policy page view
def return_policy_view(request):
    return render(request,'return_policy.html')



def student_form_submit(request):
    if request.method == 'POST':
        registration_id = request.POST.get('registration_id')
        f_name = request.POST.get('f_name')
        l_name = request.POST.get('l_name')

        student = Student(
            registration_id=registration_id,
            f_name=f_name,
            l_name=l_name
        )
        student.save()

        return redirect('student list')  
    
    return render(request, 'student/form.html') 


def student_list_view(request):
    student = Student.objects.all()
    return render(request,'student/student_list.html',{'student_variable': student})

def employee_form_submit(request):
    if request.method == 'POST':
        Emp_id = request.POST.get('Emp_id')
        emp_first_name = request.POST.get('emp_first_name')
        emp_last_name = request.POST.get('emp_last_name')
        emp_city=request.POST.get('emp_city')
        salary=request.POST.get('salary')
        cmp_name=request.POST.get('cmp_name')

        employee = Employee(
            Emp_id=Emp_id,
            emp_first_name=emp_first_name,
            emp_last_name=emp_last_name,
            emp_city=emp_city,
            salary=salary,
            cmp_name=cmp_name
        )
        employee.save()

        return redirect('employee list')  
    
def employee_edit_form(request, id):
    employee = get_object_or_404(Employee, id=id)  # Fetch the employee by ID

    if request.method == 'POST':
        employee.Emp_id = request.POST.get('Emp_id')
        employee.emp_first_name = request.POST.get('emp_first_name')
        employee.emp_last_name = request.POST.get('emp_last_name')
        employee.emp_city = request.POST.get('emp_city')
        employee.salary = request.POST.get('salary')
        employee.cmp_name = request.POST.get('cmp_name')

        employee.save()
        return redirect('employee list')

    return render(request, 'employee/emp_edit.html', {'employee': employee})

def employee_delete(request, id):
    employee = get_object_or_404(Employee, id=id)
    if request.method == 'POST':
        
        
        employee.delete()
    return redirect('employee list')

def employee_list_view(request):
    employee = Employee.objects.all()
    return render(request,'employee/list.html',{'employee_variable': employee})




def categories_view(request):
    category = Category.objects.all()
    return render(request,'categories.html', {'category_variable': category})

def category_product_view(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    products = Category_Product.objects.filter(product_category_name=category)
    
    return render(request, 'category_product.html', {
        'category': category,
        'products_variable': products
    })



def get_user_cart(request):
    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user)
    else:
        # For guest cart — this is optional and simple for now
        cart, created = Cart.objects.get_or_create(user=None)
    return cart

def add_to_cart(request, product_id):

    product = get_object_or_404(Category_Product, id=product_id)
    cart = get_user_cart(request)
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    
    return redirect('view_cart')  # You can redirect to 'category_product' if preferred


def view_cart(request):
    cart = get_user_cart(request)
    items = CartItem.objects.filter(cart=cart)
    total = cart.get_total()

    return render(request, 'add_to_cart.html', {
        'cart_items': items,
        'grand_total': total,
    })





from django.contrib.auth.decorators import login_required
from .models import Category_Product, Wishlist

@login_required
def add_to_wishlist(request, product_id):
    product = get_object_or_404(Category_Product, id=product_id)
    Wishlist.objects.get_or_create(user=request.user, product=product)
    return redirect('wishlist')  # Redirect to wishlist page

@login_required
def remove_from_wishlist(request, product_id):
    product = get_object_or_404(Category_Product, id=product_id)
    Wishlist.objects.filter(user=request.user, product=product).delete()
    return redirect('wishlist')

@login_required
def wishlist_view(request):
    wishlist_items = Wishlist.objects.filter(user=request.user)
    return render(request, 'wishlist.html', {'wishlist_items': wishlist_items})




def checkout_view(request):
    return render(request, 'checkout.html')
# place order
@login_required
@require_POST
# def place_order(request):
#     messages.success(request, "Order placed successfully!")
#     return redirect('order_success') 



@login_required
def place_order(request):
    cart = get_object_or_404(Cart, user=request.user)
    cart_items = CartItem.objects.select_related('product').filter(cart=cart)

    if not cart_items.exists():
        messages.error(request, "Your cart is empty.")
        return redirect('view_cart')

    if request.method == 'POST':
        # Get form data
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        city = request.POST.get('city')
        pincode = request.POST.get('pincode')
        country = request.POST.get('country', 'India')
        payment_method = request.POST.get('payment_method')

        # Calculate total
        total_amount = sum(item.product.selling_price * item.quantity for item in cart_items)

        # Create order
        order = Order.objects.create(
            user=request.user,
            full_name=full_name,
            email=email,
            phone=phone,
            address=address,
            city=city,
            pincode=pincode,
            country=country,
            payment_method=payment_method,
            total_amount=total_amount,
            status='Pending'
        )

        # Add items to order
        for item in cart_items:
            OrderItem.objects.create(
                order=order,
                product=item.product,
                quantity=item.quantity,
                price=item.product.selling_price
            )

        # Clear cart
        cart_items.delete()

        messages.success(request, "Order placed successfully!")
        return redirect('order_success')

    return redirect('checkout')

# from django.shortcuts import render, redirect
# from .models import Cart, CartItem, Order, OrderItem
# from django.contrib.auth.decorators import login_required
# from django.contrib import messages
# from decimal import Decimal

# @login_required
# def place_order(request):
#     if request.method == "POST":
#         user = request.user
#         full_name = request.POST.get("full_name")
#         email = request.POST.get("email")
#         phone = request.POST.get("phone")
#         address = request.POST.get("address")
#         city = request.POST.get("city")
#         state = request.POST.get("state")
#         pincode = request.POST.get("pincode")
#         country = request.POST.get("country", "India")
#         payment_method = request.POST.get("payment_method", "COD")

#         cart = Cart.objects.filter(user=user).first()
#         if not cart:
#             messages.error(request, "Cart is empty.")
#             return redirect("checkout")

#         cart_items = CartItem.objects.filter(cart=cart)
#         if not cart_items.exists():
#             messages.error(request, "Cart is empty.")
#             return redirect("checkout")

#         total_amount = sum(item.get_subtotal() for item in cart_items)

#         order = Order.objects.create(
#             user=user,
#             email=email,
#             phone=phone,
#             full_name=full_name,
#             address=address,
#             city=city,
#             pincode=pincode,
#             country=country,
#             payment_method=payment_method,
#             total_amount=total_amount
#         )

#         for item in cart_items:
#             OrderItem.objects.create(
#                 order=order,
#                 product=item.product,
#                 quantity=item.quantity,
#                 price_at_purchase=item.product.selling_price
#             )

#         # Clear cart
#         cart_items.delete()
#         cart.delete()

#         messages.success(request, "Order placed successfully!")
#         return redirect("order_success")  # Create this URL/view
#     else:
#         return redirect("checkout")


    
# def product_detail(request, product_id):
#     product = get_object_or_404(Category_Product, id=product_id)
    
#     # Calculate discount percentage if there's an original price
#     if hasattr(product, 'get_discount_percentage'):
#         discount = product.get_discount_percentage()
#     else:
#         discount = None
    
#     context = {
#         'product': product,
#         'discount': discount,
#     }
#     return render(request, 'products_detail_page.html', context)










