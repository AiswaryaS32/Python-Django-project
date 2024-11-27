from django.urls import path
from fapp import views

urlpatterns =[
    path('index/', views.index , name = 'index') ,
    path('addcat/', views.addcat , name = 'addcat') ,
    path('savecat/', views.save_category , name = 'savecat') ,
    path('viewcat/',views.viewcat, name='viewcat'),
    path('deletecat/<int:c_id>/',views.deletecat, name='deletecat'),
    path('editcat/<int:ca_id>/',views.editcat, name='editcat'),
    path('updatecat/<int:cat_id>/',views.updatecat, name='updatecat'),
    path('addpro/',views.add_product, name='addpro'),
    path('savepro/',views.save_pro, name='savepro'),
    path('viewpro/',views.viewpro, name='viewpro'),
    path('deletepro/<int:pd_id>/',views.deletepro, name='deletepro'),
    path('editpro/<int:p_id>/',views.editpro, name='editpro'),
    path('updatepro/<int:pr_id>/',views.updatepro, name='updatepro'),
    path('adminlogin/',views.loginpage, name='adminlogin'),
    path('login/',views.adminlogin, name='login'),
    path('admin_logout/',views.admin_logout, name='admin_logout'),
    path('display_contact/',views.display_contact, name='display_contact'),
    path('delete_contact/<int:co_id>/',views.delete_contact, name='delete_contact'),

]