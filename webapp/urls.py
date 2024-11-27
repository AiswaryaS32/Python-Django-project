from django.urls import path
from webapp import views

urlpatterns = [
    path('homepage/', views.homepage , name='homepage'),
    path('product_page/', views.product_page , name='product_page'),
    path('contact_page/', views.contact_page , name='contact_page'),
    path('about_page/', views.about_page , name='about_page'),
    path('save_contact/', views.save_contact , name='save_contact'),
    path('product_filter/<cat_name>/', views.product_filter , name='product_filter'),
    path('single_product/<int:pro_id>/', views.single_product , name='single_product'),
    path('signup_page/', views.signup_page , name='signup_page'),
    path('', views.login_page , name='login_page'),
    path('save_signup/', views.save_signup , name='save_signup'),
    path('userlogin/', views.userlogin , name='userlogin'),
    path('logout/', views.logout , name='logout'),
    path('save_cart/', views.save_cart , name='save_cart'),
    path('cart_page/', views.cart_page , name='cart_page'),
    path('checkout_page/', views.checkout_page , name='checkout_page'),
    path('remove_cart/<int:ct_id>/', views.remove_cart , name='remove_cart'),
    path('save_placeorder/', views.save_placeorder , name='save_placeorder'),
    path('payment/', views.payment, name='payment'),
]
