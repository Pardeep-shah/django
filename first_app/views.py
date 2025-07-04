from django.shortcuts import render,redirect,get_object_or_404
from .models import Student
from .models import *


# Create your views here.


# def about_view(request):
#     return render (request,'about.html')


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




from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Cart, CartItem, Checkout, OrderItem

@login_required
def checkout_view(request):
    cart = get_object_or_404(Cart, user=request.user)
    cart_items = cart.cartitem_set.all()
    total = sum(item.get_subtotal() for item in cart_items)

    if request.method == 'POST':
        # Save checkout details
        checkout = Checkout.objects.create(
            user=request.user,
            full_name=request.POST['full_name'],
            email=request.POST['email'],
            phone=request.POST['phone'],
            address=request.POST['address'],
            city=request.POST['city'],
            state=request.POST['state'],
            postal_code=request.POST['postal_code'],
            country=request.POST.get('country', 'India'),
            total_amount=total,
            payment_method=request.POST['payment_method'],
            payment_status='Pending',
        )

        # Create order items
        for item in cart_items:
            OrderItem.objects.create(
                order=checkout,
                product=item.product,
                quantity=item.quantity,
                price_at_purchase=item.product.selling_price,
            )

        cart.delete()  # Clear cart after checkout
        return redirect('order_success')

    return render(request, 'checkout.html', {
        'cart_items': cart_items,
        'total': total
    })


@login_required
def order_success(request):
    return render(request, 'order_success.html')

