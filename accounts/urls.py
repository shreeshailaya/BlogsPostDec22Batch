from django.urls import path
from accounts import views

urlpatterns = [
    path('login/', views.loginFunction, name= 'login'),
    path('logout/', views.logoutFunction, name='logout')
]