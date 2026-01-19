from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('guest/', views.guest_login, name='guest_login'),
    path('logout/', views.logout_view, name='logout'),
    path('products/', views.products_view, name='products'),
]