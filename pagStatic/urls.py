from django.urls import path
from . import views

urlpatterns = [
	path('', views.FirstPage, name='index'),
	path('DashBoard/', views.index, name='index'),
	path('WebPay/<int:pk>/', views.WebPay, name='WebPay'),
	path('BancoLogin/<int:pk>/', views.BancoLogin, name='BancoLogin'),
	path('BancoPago/<int:pk>/', views.BancoPago, name='BancoPago'),
]
