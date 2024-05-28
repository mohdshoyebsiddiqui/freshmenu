"""freshmenuu URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from . import views

urlpatterns = [
    path('', views.home ,name="home"),


    path('search', views.search, name='search' ),
    path('product/<id>', views.product , name="singleproduct" ),
    path('cart/<id>', views.cart , name='cart'),
    path('cartplus/<id>', views.cartplus , name='cartplus'),
    path('cartminus/<id>', views.cartminus , name='cartminus'),
    path('checkout', views.checkout ),
    path('signin', views.signin ,name='signin' ),
    path('signup', views.signup,name='signup' ),
    path('logout', views.logouts,name='logout' ),
    path('profile', views.profile,name='profile' ),
    path('order', views.order, name='oldhistory' ),
    path('addwish/<id>', views.addwish, name='addwish' ),
    path('wishlist', views.wishlist, name='wishlist' ),
    path('userlist', views.userlist, name='userlist'),
    path('friend', views.friend, name='friend'),
    path('follow', views.follow, name='follow'),
    path('profileedit/<id>', views.profileedit, name='profileedit'),
    path('userprofile/<id>', views.userprofile, name='userprofile'),

    path('orderplaced', views.orderplaced, name='orderplaced' ),
    # dashboard
    path('dashboard/',views.dashboard, name='dashboard'),
    path('dashboard/product-create',views.productcreate,name="productcreate"),
    path('dashboard/product-edit/<id>',views.productedit ,name="productedit") , 
    path('dashboard/product',views.productview,name='product') ,
    path('dashboard/product-delete/<id>',views.productdelete,name="productdelete") ,
    path('dashboard/category-create',views.categorycreate,name="categorycreate"),
    path('dashboard/category-edit/<id>',views.categoryedit,name="categoryedit") , 
    path('dashboard/category',views.categoryview,name="category") ,
    path('dashboard/category-delete/<id>',views.categorydelete,name="categorydelete") ,
    path('dashboard/user',views.userdash,name="userdash") ,
    path('dashboard/userdelete/<id>',views.userdelete,name='userdelete') ,
    path('dashboard/currentorder',views.currentorder,name='current') ,
    path('dashboard/orderconfirm/<id>',views.orderconfirm,name='orderconfirm'),
    path('dashboard/ordercancel/<id>',views.ordercancel,name='ordercancel') ,
    path('dashboard/oldorder',views.oldorder,name='old') ,
    path('dashboard/cancelorder',views.cancelorder,name='cancel') ,
    path('dashboard/signin',views.signindash,name='signindash') ,
    path('dashboard/signup',views.signupdash,name='signupdash') ,
  ]

