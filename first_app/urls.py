from django.contrib import admin
from django.urls import path,include
# from .views import home_view
from .views import *

from .views import add_to_cart_view

# path('url', fxn_name, 'route name for html file ')


urlpatterns = [
   path('pradeep', homePage_view, name= 'home_page'),
   path('contact_us', contact_us_view, name='contact_us_page'),

    path('about_us', about_fxn, name='about_us_page'),

    path('privacy_policy', privacy_policy_view, name='privacy_policy_page'),



    path('our_vision', our_vision_view, name='our_vision_page'),



    path('our_mission', our_mission_view, name='our_mission_page'),


    path('return_poloicy', return_policy_view, name='return_policy_page'),
    path('categories', categories_view, name='categories'),
    path('student_form', student_form_submit, name='Student form'),

    path('student_list', student_list_view, name = 'student list'),

    path('employee_form', employee_form_submit,name='employee form' ),

    path('employee_list', employee_list_view, name= 'employee list'),
    path('employee_edit', employee_edit_form, name= 'employee list'),
    path('employee_edit/<int:id>/', employee_edit_form, name='edit_employee'),

    path('employee_delete/<int:id>/', employee_delete, name='delete_employee'),

    path('categories/<int:category_id>/products/', category_product_view, name='category_products'),

    


    path('cart/', add_to_cart_view, name='cart'),

 


]