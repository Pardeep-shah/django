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


def add_to_cart_view(request):
    cart_items = Cart.objects.filter(user=request.user)
    grand_total = sum(item.subtotal for item in cart_items)
    return render(request, 'add_to_cart.html', {'cart_items': cart_items, 'grand_total': grand_total})

