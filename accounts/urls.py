from django.urls import path
from . import views

urlpatterns=[

     path('customer_register/',views.Customer_register.as_view(), name='customer_register'),
     path('manager_register/',views.Manager_register.as_view(), name='manager_register'),
     path('login',views.login_request,name='login'),
     path('logout',views.logout_view,name='logout'),

]