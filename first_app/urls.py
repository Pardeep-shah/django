from django.contrib import admin
from django.urls import path,include
# from .views import home_view
from .views import *



# path('url', fxn_name, 'route name for html file ')


urlpatterns = [
   path('register/', register_view, name='register'),
   path('login/', login_view, name='login'),
   path('logout/', logout_view, name='logout'),


   path('Home', homePage_view, name= 'home_page'),
   path('contact-us', contact_us_view, name='contact_us_page'),

    path('about-us', about_us_view, name='about_us_page'),


    path('shop', shop_now_view, name='shop_now_page'),


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

    path('category/<int:category_id>/', category_product_view, name='category_product'),
    path('add-to-cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('cart/', view_cart, name='view_cart'),

    


    path('wishlist/', wishlist_view, name='wishlist'),
    path('add-to-wishlist/<int:product_id>/', add_to_wishlist, name='add_to_wishlist'),
    path('remove-from-wishlist/<int:product_id>/', remove_from_wishlist, name='remove_from_wishlist'),

    path('checkout/', checkout_view, name='checkout'),
    path('place-order/', place_order, name='place_order'),


    
    path('my_orders/', my_orders, name='my_orders'),
    path('profile/', profile_view, name='profile'),

    path('contact-us/', contact_us_view, name='contact_us'),

    path('edit-profile/', edit_profile, name='edit_profile'),





 
 ]



  

    

 


