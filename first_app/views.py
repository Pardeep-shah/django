from django.shortcuts import render

# Create your views here.


def about_view(request):
    return render (request,'about.html')

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

def categories_view(request):
    return render(request,'categories.html')


def student_form_view(request):
    return render(request,'student/form.html')