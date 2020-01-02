from django.urls import path
from .import views

urlpatterns = [
    path('',views.index,name='index'),
    path('sin_up',views.sin_up,name='sin_up'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
]