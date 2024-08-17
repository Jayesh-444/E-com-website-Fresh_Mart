from django.contrib import admin
from django.urls import path, include
from .import views 
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('', include('django.contrib.auth.urls')),

    path('',views.INDEX,name='index'),

    path('master/',views.MASTER,name='master'),

    path('about/',views.ABOUT,name='about'),

    path('shop/',views.SHOP,name='shop'),

    path('gallery/',views.GALLERY,name='gallery'),

    path('contactus/',views.CONTACT_US,name='contactus'),


    path('checkout/',views.CHECKOUT,name='checkout'),

    path('myaccount/',views.MYACCOUNT,name='myaccount'),
    
    path('wishlist/',views.WISHLIST,name='wishlist'), 


    path('add/<int:id>/', views.cart_add, name='cart_add'),
    path('item_clear/<int:id>/', views.item_clear, name='item_clear'),
    path('item_increment/<int:id>/',views.item_increment, name='item_increment'),
    path('item_decrement/<int:id>/',views.item_decrement, name='item_decrement'),
    path('cart_clear/', views.cart_clear, name='cart_clear'),
    path('cart/',views.cart_detail,name='cart'),

    
    path('orderplace/',views.place_order,name='orderplace'),




] + static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
