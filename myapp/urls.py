from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    
    # path('', views.home), # function based view
    path('',views.ProductView.as_view(),name="home"), # class based view
    path('product-detail/<int:pk>', views.ProductDetailView.as_view(), name='product-detail'),
    path('cart/', views.add_to_cart, name='add-to-cart'),
    path('buy/', views.buy_now, name='buy-now'),
    path('profile/', views.profile, name='profile'),
    path('address/', views.address, name='addaress'),
    path('orders/', views.orders, name='orders'),
    path('changepassword/', views.change_password, name='changepassword'),
    
    path('mobile/',views.mobile,name='mobile'),
    path('mobile/<slug:data>', views.mobile, name='mobiledata'),

    path('laptop/',views.laptop,name='laptop'),
    path('laptop/<slug:data>',views.laptop,name='laptopdata'),

    path('bottomwear/',views.bottomwear,name='bottomwear'),
    path('bottomwear/<slug:data>', views.bottomwear,name='bottomweardata'),

    path('topwear/',views.topwear,name='topwear'),
    path('topwear/<slug:data>',views.topwear,name='topweardata'),

    path('login/', views.login, name='login'),
    path('registration/', views.CustomerRegistrationView.as_view(), name='customerregistration'),
    path('checkout/', views.checkout, name='checkout'),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)