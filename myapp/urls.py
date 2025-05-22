"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('blog_details', views.blog_details, name='blog_details'),
    path('blog', views.blog, name='blog'),
    path('checkout', views.checkout, name='checkout'),
    path('contact', views.contact, name='contact'),
    path('index', views.index, name='index'),
    path('main', views.main, name='main'),
    path('shop_details', views.shop_details, name='shop_details'),
    path('shop_grid', views.shop_grid, name='shop_grid'),
    path('shoping_cart', views.shoping_cart, name='shoping_cart'),
    path('register', views.register, name='register'),
    path('', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('profile', views.profile, name='profile'),
    path('f_password', views.f_password, name='f_password'),
    path('confirm_password', views.confirm_password, name='confirm_password'),
    path('search_fun', views.search_fun, name='search_fun'),
    path('wishlists', views.wishlists, name='wishlists'),
    path('add_wishlist/<int:id>', views.add_wishlist, name='add_wishlist'),
    path('add_cart/<int:id>', views.add_cart, name='add_cart'),
    path('cart_plus/<int:id>', views.cart_plus, name='cart_plus'),
    path('cart_minus/<int:id>', views.cart_minus, name='cart_minus'),
]
