
from django.urls import path,include
from .  import views


urlpatterns = [
   path('',views.userlogin, name='login'),
   path('signup/', views.usersignup, name = 'signup'),
   path('home/',views.home , name = 'home'),
   path('logout/', views.logout, name='logout'),
   path('adminlogin/',views.admin_login, name = 'admin'),
   path('usermanagment/',views.adminpage, name = 'adminpage' ),
   path('adduser/', views.useradd, name= 'adduser'),
   path('adminlogout/',views.adminlogout, name = 'adminlogout'),
   path('updateuser/<int:pk>',views.updateuser, name = 'updateuser'),
   path('deleteuser/<int:pk>', views.deleteuser, name = 'deleteuser')

   
]
