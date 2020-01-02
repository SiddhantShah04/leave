from django.urls import path
from .import views

urlpatterns = [
    path('show',views.show,name='show'),
    path('profile',views.profile,name='profile'),
    path('passwordemp',views.passwordemp,name='passwordemp'), 
    path('emp_all_leave',views.emp_all_leave,name='emp_all_leave'),      
]